"""Test for translate.py."""

from .translate import change as t
import string
import random


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


def test_letters():
    """Testing of most possible combinations."""
    assert t('aaa bbb ccc ddd eee fff ggg hhh iii jjj kkk lll mmm nnn ooo'
             ' ppp qqq rrr sss ttt uuu vvv www xxx yyy zzz') == 'kikiki' \
        ' ululul vavava popopo momama asusus bavobav  ononon bovbovbov' \
        ' aeaeae kakaka bebobo bobebe dodede sii ssssss chochoch shash' \
        ' pinono nnn uuu nnnnnn ererer ththth watwatwat'


def test_numbers():
    """Testing of numbers."""
    assert t('1 2 3 4 5 6 7 8 9 0') == 'dobomo pinndo pichmoma asdonch' \
        ' asonumo shoner shmoumabo moonbavpi boonbemo watmochdo'


def test_big_numbers():
    """Testing larger numbers and special cases."""
    assert t('150') == 'dobomo nbopochmopo kibopo asonuspith'
    assert t('6874.893') == 'shoner pidonshkibopo, moonbavpi nbopochmopo' \
        ' kibopo shmoumabopith-asdonch sdoonbopi moonbavpi boonbemo pichmoma'
    assert t('i have 12 apples') == 'on kiumo pinnmokauma kisikamosh'
    assert t('i have 6.5 apples.') == 'on kiumo shoner sdoonbopi asonumo' \
        ' kisikamosh.'
    assert t('i have .57 apples') == 'on kiumo watmochdo sdoonbopi asonumo' \
        ' shmoumabo kisikamosh'
    assert t('there are 27.') == 'pimochma kichmo pinnmobonoth-shmoumabo.'
    assert t('there are .5.') == 'pimochma kichmo watmochdo sdoonbopi asonumo.'
    assert t('there are 3892.4685.') == 'pimochma kichmo pichmoma' \
        ' pidonshkibopo, moonbavpi nbopochmopo kibopo boonbemopith-pinndo' \
        ' sdoonbopi asdonch shoner moonbavpi asonumo.'
    assert t('1234567890') == 'dobomo ulonkakaondobo, pinndo nbopochmopo' \
        ' kibopo pionchnoth-asdonch beonkakaondobo, asonumo nbopochmopo' \
        ' kibopo shonerpith-shmoumabo pidonshkibopo, moonbavpi nbopochmopo' \
        ' kibopo boonbemopith'
    assert t('-127') == 'beonbonsh dobomo nbopochmopo kibopo pinnmobonoth' \
        '-shmoumabo'


def test_randoms():
    """Testing that a whole bunch of strings work and don't fail."""
    for i in range(1000):
        test_string = ''.join(random.choice(
            string.ascii_letters + string.digits + string.punctuation
            ) for _ in range(1000))
        assert t(test_string)
