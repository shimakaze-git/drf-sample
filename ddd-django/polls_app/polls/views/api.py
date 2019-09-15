
# from rest_framework.views import APIView

# class CreateUserView(APIView):
#     def post(self, request):
#         # validate input
#         user_dto, errors = CreateUserSerializer().load(request.data)
#         if errors:
#             return Response(errors, status=status.HTTP_400_BAD_REQUEST)

#         # call usecase
#         use_case = build_create_user_use_case()
#         try:
#             user = use_case.execute(user_dto)

#         # handle exceptions
#         except (UsernameAlreadyExistsError) as e:
#             return Response(str(e), status=status.HTTP_422_UNPROCESSABLE_ENTITY)
#         except permissionsInsuficientException as e:
#             return Response(str(e), status=status.HTTP_403_FORBIDDEN)

#         # return serialised data
#         else:
#             return Response(
#                 UserSerializer().dump(user).data,
#                 status=status.HTTP_201_CREATED
#             )