from .translate import change as t


def test_single_valids():
    assert t('quake') == 'ssnkiaemo'
    assert t('quack') == 'ssnkivaae'
    assert t('access') == 'kivavamosha'
    assert t('class') == 'vakakisha'
    assert t('jesus') == 'bovmoshnsh'
    assert t('green') == 'bavchmomabo'
    assert t('yellow') == 'thmokakadonn'
    assert t('') == ''


def test_long_valids():
    assert t('burnt my hand badly with bleach') == 'ulnchbopi beth kibopo ulkipokath nnonpi ulkamokiva'
    assert t('big ben is in london and it is hated') == 'ulonbav ulmobo onsh onbo kadobopodebe kibopo onpi onsh kipimopo'
    assert t('these words have too much length') == 'pimoshma nndochposh kiumo pidode benva kamobobavpi'
    assert t('i walk to seattle ferry terminal') == 'on nnkikaae pido shmokipinokama asmochochth pimochbeonbokika'
    assert t('the quick brown fox jumps over the lazy dog') == 'pimo ssnonvaae ulchdonnbo asdoer bovnbessh doumoch pimo kakiwatth podobav'
    assert t('tyler nathanial trask') == 'pithkamoch bokipikibeonkika pichkishae'
    assert t('shannon christoffer tully') == 'shkibobedobe vachonshpidoasusmooch pinkakath'
    assert t('mr kitty-cat meow-face') == 'bech aeonpinoth-vakipi bemodonn-askivamo'
    assert t('coffee tastes good') == 'vadoasusmoma pikishnomosh bavdodepo'


def test_invalid():
    assert t(1) == 'Try again. Valid inputs are letters, spaces, and dashes.'
    assert t('.') == 'Try again. Valid inputs are letters, spaces, and dashes.'
    assert t('1') == 'Try again. Valid inputs are letters, spaces, and dashes.'
    assert t('@') == 'Try again. Valid inputs are letters, spaces, and dashes.'
