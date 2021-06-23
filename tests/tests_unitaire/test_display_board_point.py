import server


class DisplayPointsClubs:

    # modification du contenu des variables

    server.clubs = [{
            "name": "Test",
            "email": "test@test.co",
            "points": "4"
        }]

    # page existe
    def test_correct_route(self, client):

        rv = client.post('/list')
        assert rv.status_code == 200

    # page non existante
    def test_incorrect_route(self, client):

        rv = client.post('/lists')
        assert rv.status_code == 500
