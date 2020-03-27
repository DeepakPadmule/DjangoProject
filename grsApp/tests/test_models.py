# from django.test import TestCase
# from rest_framework import status
#
#
# from ..models import GrievanceTypes, Grievances, GrievanceDetails
# from ..serializers import GrievancesSerializer, GrievanceDetailsSerializer, GrievanceTypesSerializer


# class GrievanceTypesTestCase(TestCase):
#     def setUp(self):
#         self.griev1 = GrievanceTypes.objects.create(griev_type="Water")
#         self.griev2 = GrievanceTypes.objects.create(griev_type="Electricity")
#
#     def test_grievance_type_creation(self):
#         griev_obj = GrievanceTypes.objects.get(griev_type="Water")
#         self.assertEqual(griev_obj.griev_type, "Water")
#
#     def test_grievance_type_list_view(self):
#         response = self.client.get("/grievanceTypes")
#         grievance_type_list = GrievanceTypes.objects.all()
#         grievance_type_list_serializer = GrievanceTypesSerializer(grievance_type_list, many=True)
#         self.assertEqual(response.data, grievance_type_list_serializer.data)
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#
#     def test_get_valid_single_grievance_type(self):
#         response = self.client.get("/grievanceTypes/" + self.griev1.pk)
#         grievance_type = GrievanceTypes.objects.get(pk=self.griev1.pk)
#         grievance_type_serializer = GrievanceTypesSerializer(grievance_type)
#         self.assertEqual(response.data, grievance_type_serializer.data)
#         # print("response.data: ", response.data)
#         # print("ser.data: ", grievance_type_serializer.data)
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#
#     def test_get_invalid_single_grievance_type(self):
#         response = self.client.get("/grievanceTypes/" + "GT-100")
#         self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
#
#     def test_post_valid_grievance_type(self):
#         griev_type_data = {"griev_type": "Road"}
#         response = self.client.post('/grievanceTypes', data=griev_type_data, format='json')
#         self.assertEqual(response.status_code, status.HTTP_201_CREATED)
#
#     def test_post_invalid_grievance_type(self):
#         griev_type_data = {"griev_type": ""}
#         response = self.client.post('/grievanceTypes', data=griev_type_data, format='json')
#         self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
#

# class GrievancesTestCase(TestCase):
#     def setUp(self):
#         self.griev_water = Grievances.objects.create(
#                                 griev_title="Water Issue",
#                                 griev_desc="Water Issue Description",
#                             )
#
#         self.griev_electricity = Grievances.objects.create(
#                                     griev_title="Electricity Issue",
#                                     griev_desc="Electricity Issue Description",
#                                 )
#
#     def test_grievance_creation(self):
#         griev_obj = Grievances.objects.get(griev_title="Water Issue")
#         griev_obj2 = Grievances.objects.get(griev_title="Electricity Issue")
#         self.assertEqual(griev_obj.griev_title, "Water Issue")
#         self.assertEqual(griev_obj2.griev_title, "Electricity Issue")
#
#     def test_grievance_list_view(self):
#         response = self.client.get("/grievances")
#         grievance_list = Grievances.objects.all()
#         grievance_serializer = GrievancesSerializer(grievance_list, many=True)
#         self.assertEqual(response.data, grievance_serializer.data)
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#
#     def test_delete_valid_grievance(self):
#         response = self.client.delete('/grievances/'+self.griev_water.pk)
#         self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
#
#     def test_delete_inavalid_grievance(self):
#         response = self.client.delete('/grievances/'+'G-100')
#         self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)


# class GrievanceDetailsTestCase(TestCase):
#     def setUp(self):
#         GrievanceDetails.objects.create(griev_status="Pending", griev_status_desc="on hold")
#         GrievanceDetails.objects.create(griev_status="Accepted", griev_status_desc="Working on it")
#
#     def test_grievance_details_creation(self):
#         griev_obj = GrievanceDetails.objects.get(griev_status="Accepted")
#         self.assertEqual(griev_obj.griev_status, "Accepted")
#
#     def test_grievance_details_list_view(self):
#         response = self.client.get("/grievanceDetails")
#         grievance_details_list = GrievanceDetails.objects.all()
#         grievance_details_serializer = GrievanceDetailsSerializer(grievance_details_list, many=True)
#         self.assertEqual(response.data, grievance_details_serializer.data)
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
