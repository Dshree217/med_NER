from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from search.serializers import MedicineListSerializer, MedicineDataSerializer
from search.models import MedicineData
from search.utils import NER


@csrf_exempt
def searchAPI(request):
    final_response = []
    if request.method == 'POST':
        data = JSONParser().parse(request)
        medicine_list = NER.ner(data['data'])
        for i in medicine_list:
            qs = list(MedicineData.objects.all().filter(salt_name=i))
            for key in qs:
                temp_obj = {}
                temp_obj['sku_id'] = key.sku_id
                temp_obj['product_id'] = key.product_id
                temp_obj['sku_name'] = key.sku_name
                temp_obj['price'] = key.price
                temp_obj['manufacturer_name'] = key.manufacturer_name
                temp_obj['salt_name'] = key.salt_name
                temp_obj['drug_form'] = key.drug_form
                temp_obj['pack_size'] = key.pack_size
                temp_obj['strength'] = key.strength
                temp_obj['product_banned_flag'] = key.product_banned_flag
                temp_obj['unit'] = key.unit
                temp_obj['price_per_unit'] = key.price_per_unit
                final_response.append(temp_obj)
    return JsonResponse({'message': 'success', 'result': final_response}, safe=False)

@csrf_exempt
def save_data(request):
    if request.method == 'POST':
        data = JSONParser().parse(request)
        employees_serializer = MedicineDataSerializer(data=data)
        if employees_serializer.is_valid():
            result_set = employees_serializer.save()
            return JsonResponse("Inserted Successfully, Request_id {}".format(result_set.autoid), safe=False)
    return JsonResponse("Failed to Insert", safe=False)
