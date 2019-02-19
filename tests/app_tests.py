from nose.tools import *
from app import app

app.config['TESTING'] = True
web = app.test_client()

def test_bonus():
    rv = web.get('/bonus/', follow_redirects=True)
    assert_equal(rv.status_code, 404)

def test_index():
    rv = web.get('/', follow_redirects=True)
    assert_equal(rv.status_code, 200)

def test_plot():
    rv = web.get('/plot/', follow_redirects=True)
    assert_equal(rv.status_code, 200)
    assert_in(b'In 16th century', rv.data)

def test_seven_samurai():
    rv = web.get('/the_seven/', follow_redirects=True)
    assert_equal(rv.status_code, 200)
    assert_in(b'The seven samurai', rv.data)

def test_stats():
    rv = web.get('/stats/', follow_redirects=True)
    assert_equal(rv.status_code, 200)
    assert_in(b'The film was directed', rv.data)

def test_cool_facts():
    rv = web.get('/cool_facts/', follow_redirects=True)
    assert_equal(rv.status_code, 200)
    assert_in(b'Fact number', rv.data)
