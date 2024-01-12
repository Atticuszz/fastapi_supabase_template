# Additional assertions based on your application's logic

# def test_create_item(test_client: TestClient,access_token: str):
#     test_data = Faker().sentence()
#     headers = get_auth_header(access_token)
#     response = test_client.post("/create-item",headers=headers,
#     json={"test_data": test_data})
#     assert response.status_code == 200
#     assert response.json()["test_data"] == "Sample Data"
#     # Additional assertions based on your application's logic
#
# def test_read_all_items(test_client):
#     response = test_client.get("/read-all-item")
#     assert response.status_code == 200
#     assert isinstance(response.json(), list)
#     # Further assertions can be added here
#
# def test_read_item_by_id(test_client):
#     # Use a valid ID for an existing item
#     response = test_client.get("/get-by-id?id=valid_id")
#     assert response.status_code == 200
#     assert response.json()["id"] == "valid_id"
#     # More assertions based on expected item details
#
# def test_read_item_by_owner(test_client):
#     response = test_client.get("/get-by-owner")
#     assert response.status_code == 200
#     assert isinstance(response.json(), list)
#     # Additional checks based on expected output
#
# def test_update_item(test_client):
#     # Use a valid ID for an existing item
#     response = test_client.put("/update-it
#     em", json={"id": "valid_id", "test_data": "Updated Data"})
#     assert response.status_code == 200
#     assert response.json()["test_data"] == "Updated Data"
#     # Additional checks and validations
#
# def test_delete_item(test_client):
#     # Use a valid ID for an existing item
#     response = test_client.delete("/delete", json={"id": "valid_id"})
#     assert response.status_code == 200
#     # Assertions to confirm deletion
