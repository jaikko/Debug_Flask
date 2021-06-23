import server


class DisplayPointsClubs:

    # modification du contenu des variables

    server.clubs = [{
            "name": "Test",
            "email": "test@test.co",
            "points": "4"
        }]

    # nombre de points suffisants
    def test_booking(self, client):

        rv = client.post('/list')
        assert rv.status_code == 200
        html = rv.get_data(as_text=True)
        assert '<td>test@test.co</td>' in html
        assert '<td>4</td>' in html
        
