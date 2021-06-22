import server

class TestPointsClubsUpdated:

    def test_booking(self, client, generate_variables):
        server.clubs, server.competitions =  generate_variables
        rv = client.post('/purchasePlaces', data=dict(
            places=3,
            competition="Spring Festival",
            club="Test"
            ))
        assert rv.status_code == 200
        html = rv.get_data(as_text=True)
        assert '<h2>Welcome, test@test.co </h2>' in html
        assert 'Points available: 10' in html
        assert '<li>Great-booking complete!</li>' in html
