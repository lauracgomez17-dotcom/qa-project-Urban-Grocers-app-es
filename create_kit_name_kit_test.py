import data
import sender_stand_request


# Función para cambiar el valor del parámetro Name en el cuerpo de la solicitud
def get_kit_body(kit_name):
    current_kit = data.kit_body.copy()
    current_kit["name"] = kit_name
    return current_kit

#Funcion para obtener el authToken
def get_new_user_token():
    response = sender_stand_request.post_new_client_kit(data.user_body)
    return response.json()["authToken"]


# Función de prueba positiva
def positive_assert(kit_body):
    response = sender_stand_request.post_new_client_kit(kit_body,get_new_user_token())
    assert response.status_code == 201


# Función de prueba negativa
def negative_assert(kit_body):
    response = sender_stand_request.post_new_client_kit(kit_body,get_new_user_token())
    assert response.status_code == 400

#PRUEBAS

#1 El número permitido de caracteres (1)
def test_create_kit_1_letter_in_the_name():
    current_kit_body = get_kit_body("K")
    positive_assert(current_kit_body)


#2 El número permitido de caracteres (511)
def test_create_kit_511_letter_in_the_name():
    current_kit_body = get_kit_body ("AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabC")
    positive_assert(current_kit_body)


#3 El número de caracteres es menor que la cantidad permitida (0):
def test_create_kit_less_letter_in_the_name():
    current_kit_body = get_kit_body("")
    negative_assert(current_kit_body)


#4 El número de caracteres es mayor que la cantidad permitida (512)
def test_create_kit_512_letter_in_the_name():
    current_kit_body = get_kit_body("AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcD")
    negative_assert(current_kit_body)


#5 Se permiten caracteres especiales
def test_create_kit_special_character_in_the_name():
    current_kit_body = get_kit_body("Kit#$%")
    positive_assert(current_kit_body)


#6 Se permiten espacios
def test_create_kit_spaces_in_the_name():
    current_kit_body = get_kit_body("Nuevo Kit")
    positive_assert(current_kit_body)


#7 Se permiten números
def test_create_kit_numbers_in_the_name():
    current_kit_body = get_kit_body("17")
    positive_assert(current_kit_body)


#8 El parámetro no se pasa en la solicitud
def test_the_parameter_is_not_passed_in_the_request():
    current_kit_body = get_kit_body({})
    negative_assert(current_kit_body)


#9 Se ha pasado un tipo de parámetro diferente (número)
def test_a_parameter_type_other_than_number_has_been_passed_():
    current_kit_body = get_kit_body(123)
    negative_assert(current_kit_body)



