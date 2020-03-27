from django.test import TestCase
from rest_framework import status

from ..models import GrievanceDetails
from ..serializers import GrievanceDetailsSerializer


class GrievanceDetailsTestCase(TestCase):
    def setUp(self):
        GrievanceDetails.objects.create(griev_status="Pending", griev_status_desc="on hold")
        GrievanceDetails.objects.create(griev_status="Accepted", griev_status_desc="Working on it")

    def test_grievance_details_creation(self):
        griev_obj = GrievanceDetails.objects.get(griev_status="Accepted")
        self.assertEqual(griev_obj.griev_status, "Accepted")

    def test_grievance_details_list_view(self):
        response = self.client.get("/grievanceDetails")
        grievance_details_list = GrievanceDetails.objects.all()
        grievance_details_serializer = GrievanceDetailsSerializer(grievance_details_list, many=True)
        self.assertEqual(response.data, grievance_details_serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
