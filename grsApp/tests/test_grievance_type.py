from django.test import TestCase
from rest_framework import status

from ..models import GrievanceTypes
from ..serializers import GrievanceTypesSerializer


class GrievanceTypesTestCase(TestCase):
    def setUp(self):
        self.griev1 = GrievanceTypes.objects.create(griev_type="Water")
        self.griev2 = GrievanceTypes.objects.create(griev_type="Electricity")

    def test_grievance_type_creation(self):
        griev_obj = GrievanceTypes.objects.get(griev_type="Water")
        self.assertEqual(griev_obj.griev_type, "Water")

    def test_grievance_type_list_view(self):
        response = self.client.get("/grievanceTypes")
        grievance_type_list = GrievanceTypes.objects.all()
        grievance_type_list_serializer = GrievanceTypesSerializer(grievance_type_list, many=True)
        self.assertEqual(response.data, grievance_type_list_serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_valid_single_grievance_type(self):
        response = self.client.get("/grievanceTypes/" + self.griev1.pk)
        grievance_type = GrievanceTypes.objects.get(pk=self.griev1.pk)
        grievance_type_serializer = GrievanceTypesSerializer(grievance_type)
        self.assertEqual(response.data, grievance_type_serializer.data)
        # print("response.data: ", response.data)
        # print("ser.data: ", grievance_type_serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_invalid_single_grievance_type(self):
        response = self.client.get("/grievanceTypes/" + "GT-100")
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_post_valid_grievance_type(self):
        griev_type_data = {"griev_type": "Road"}
        response = self.client.post('/grievanceTypes', data=griev_type_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_post_invalid_grievance_type(self):
        griev_type_data = {"griev_type": ""}
        response = self.client.post('/grievanceTypes', data=griev_type_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

