import sender_stand_request
import data

def get_kit_body(name):
    current_body = data.kit_body.copy()
    current_body["name"] = name
    return current_body

def get_new_user_token():
    response = sender_stand_request.post_new_user(data.user_body)
    return response.json()["authToken"]

def positive_assert(kit_body):
    response = sender_stand_request.post_new_client_kit(kit_body, get_new_user_token())
    assert response.status_code == 201
    assert response.json()["name"] == kit_body["name"]

def negative_assert_code_400(kit_body):
    response = sender_stand_request.post_new_client_kit(kit_body, get_new_user_token())
    assert response.status_code == 400

def test_crear_kit_con_1_letra():
    new_kit_body = get_kit_body("A")
    positive_assert(new_kit_body)

def test_crear_kit_con_el_maximo_511_letra():
    new_kit_body = get_kit_body("AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabC")
    positive_assert(new_kit_body)

def test_crear_kit_con_nombre_en_blanco():
    new_kit_body = get_kit_body("")
    negative_assert_code_400(new_kit_body)

def test_crear_kit_con_512_letras_mayor_a_lo_permitido():
    new_kit_body = get_kit_body("AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcD")
    negative_assert_code_400(new_kit_body)

def test_crear_kit_con_caracteres_especiales():
    new_kit_body = get_kit_body("№%@,!?")
    positive_assert(new_kit_body)

def test_crear_kit_con_espacios():
    new_kit_body = get_kit_body("A Aaa")
    positive_assert(new_kit_body)

def test_crear_kit_con_numeros():
    new_kit_body = get_kit_body("123")
    positive_assert(new_kit_body)

def test_crear_sin_el_parametro_name_en_la_solicitud():
    current_kit_body = data.kit_body.copy()
    current_kit_body.pop("name")
    negative_assert_code_400(current_kit_body)

def test_crear_kit_con_tipo_de_parametro_numero():
    new_kit_body = get_kit_body(123)
    negative_assert_code_400(new_kit_body)