"""Test for translate.py."""

from .translate import change as t


def test_single_valids():
    """Test single word strings."""
    assert t('quake') == 'ssnkiaemo'
    assert t('quack') == 'ssnkivaae'
    assert t('access') == 'kivavamosha'
    assert t('class') == 'vakakisha'
    assert t('jesus') == 'bovmoshnsh'
    assert t('green') == 'bavchmomabo'
    assert t('yellow') == 'thmokakadonn'


def test_long_valids():
    """Test multi word strings."""
    assert t('burnt my hand badly with bleach') == 'ulnchbopi beth kibopo' \
        ' ulkipokath nnonpi ulkamokiva'
    assert t('big ben is in london and it is hated') == 'ulonbav ulmobo' \
        ' onsh onbo kadobopodebe kibopo onpi onsh kipimopo'
    assert t('these words have too much length') == 'pimoshma nndochposh' \
        ' kiumo pidode benva kamobobavpi'
    assert t('i walk to seattle ferry terminal') == 'on nnkikaae pido' \
        ' shmokipinokama asmochochth pimochbeonbokika'
    assert t('the quick brown fox jumps over the lazy dog') == 'pimo' \
        ' ssnonvaae ulchdonnbo asdoer bovnbessh doumoch pimo kakiwatth podobav'
    assert t('mr kitty-cat meow-face') == 'bech aeonpinoth-vakipi bemodonn-' \
        'askivamo'
    assert t('coffee tastes good') == 'vadoasusmoma pikishnomosh bavdodepo'


def test_invalid():
    """Test invalid inputs."""
    fail = 'Try again. Valid inputs are letters, spaces, and dashes.'
    assert t(1) == fail
    assert t('.') == fail
    assert t('1') == fail
    assert t('@') == fail
    assert t('') == fail


def test_letters():
    """Testing of most possible combinations."""
    assert t('aaa bbb ccc ddd eee fff ggg hhh iii jjj kkk lll mmm nnn ooo'
             ' ppp qqq rrr sss ttt uuu vvv www xxx yyy zzz') == 'kikiki' \
        ' ululul vavava popopo momama asusus bavobav  ononon bovbovbov' \
        ' aeaeae kakaka bebobo bobebe dodede sii ssssss chochoch shash' \
        ' pinono nnn uuu nnnnnn ererer ththth watwatwat'