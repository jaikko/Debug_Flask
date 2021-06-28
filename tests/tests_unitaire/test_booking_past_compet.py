import server


class TestBookingPastCompet:

    # modification du contenu des variables
    def setup(self):
        server.competitions = [{
                "name": "Spring Festival",
                "date": "2020-03-27 10:00:00",
                "numberOfPlaces": "15"
                },
                {
                "name": "Spring",
                "date": "2022-03-27 10:00:00",
                "numberOfPlaces": "12"
            }]

        server.clubs = [{
                "name": "Test",
                "email": "test@test.co",
                "points": "14"
            }]

    # réserver une compétition expirée
    def test_correct_compet(self, client):

        rv = client.post('/purchasePlaces', data=dict(
            places=3,
            competition="Spring",
            club="Test"
            ))
        assert rv.status_code == 200

    # réserver une compétition expirée
    def test_incorrect_compet(self, client):

        rv = client.post('/purchasePlaces', data=dict(
            places=5,
            competition="Spring Festival",
            club="Test"
            ))
        assert rv.status_code == 200
        html = rv.get_data(as_text=True)
        assert '<li>You don&#39;t have enougth point or the number entered is greater than the number of places remaining</li>' in html
