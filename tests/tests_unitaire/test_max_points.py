import server


class TestPointsClubs:

    # nombre de points inférieurs à 12
    def test_correct_number(self, client, generate_variables):
        server.clubs, server.competitions = generate_variables
        rv = client.post('/purchasePlaces', data=dict(
            places=3,
            competition="Spring Festival",
            club="Test"
            ))
        assert rv.status_code == 200

    # nombre de points supérieur à 12
    def test_incorrect_number(self, client, generate_variables):
        server.clubs, server.competitions = generate_variables
        rv = client.post('/purchasePlaces', data=dict(
            places=13,
            competition="Spring Festival",
            club="Test"
            ))
        assert rv.status_code == 200
        html = rv.get_data(as_text=True)
        assert '<li>You can&#39;t reserve more than 12 places</li>' in html
