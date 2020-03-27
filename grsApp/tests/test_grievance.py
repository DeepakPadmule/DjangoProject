from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.fields import DateTimeField
from rest_framework.utils import json

from ..models import Grievances
from ..serializers import GrievancesSerializer


class GrievancesTestCase(TestCase):
    def setUp(self):
        self.griev_water = Grievances.objects.create(
                                griev_title="Water Issue",
                                griev_desc="Water Issue Description",
                            )

        self.griev_electricity = Grievances.objects.create(
                                    griev_title="Electricity Issue",
                                    griev_desc="Electricity Issue Description",
                                )

        # self.griev_valid = Grievances.objects.create(
        #     griev_title="Water Issue Updated",
        #     griev_desc="Water Issue Description Updated",
        #    # griev_type_id="GT-0002",
        #     griev_filed_date="12-05-1995"
        # )

    def test_grievance_creation(self):
        griev_obj = Grievances.objects.get(griev_title="Water Issue")
        griev_obj2 = Grievances.objects.get(griev_title="Electricity Issue")
        self.assertEqual(griev_obj.griev_title, "Water Issue")
        self.assertEqual(griev_obj2.griev_title, "Electricity Issue")

    def test_grievance_list_view(self):
        response = self.client.get("/grievances")
        grievance_list = Grievances.objects.all()
        grievance_serializer = GrievancesSerializer(grievance_list, many=True)
        self.assertEqual(response.data, grievance_serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_valid_grievance(self):
        response = self.client.delete('/grievances/'+self.griev_water.pk)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_delete_invalid_grievance(self):
        response = self.client.delete('/grievances/'+'G-100')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

