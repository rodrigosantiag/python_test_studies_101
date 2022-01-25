from src.leilao.dominio import Usuario, Leilao

import pytest

from src.leilao.excecoes import LanceInvalido


@pytest.fixture
def vini():
    return Usuario("Vini", 100.0)


@pytest.fixture
def leilao():
    return Leilao("Celular")


def test_deve_subtrair_valor_da_carteria_do_usuario_quando_este_propor_um_lance(vini, leilao):
    vini.propoe_lance(leilao, 50.0)

    assert vini.carteira == 50.0


def test_deve_permitir_propor_lance_quando_valor_menor_que_valor_carteira(vini, leilao):
    vini.propoe_lance(leilao, 1.0)

    assert vini.carteira == 99.0


def test_deve_permitir_propor_lance_quando_valor_igual_valor_carteira(vini, leilao):
    vini.propoe_lance(leilao, 100.0)

    assert vini.carteira == 0.0


def test_nao_deve_permitir_propor_lance_quando_valor_maior_valor_carteira(vini, leilao):
    with pytest.raises(LanceInvalido):
        vini.propoe_lance(leilao, 200.0)
