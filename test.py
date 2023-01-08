
import script
import opera
import configparser
import os

def test_parse_sensor_data():
    assert parse_sensor_data(0b00000001) == "No issues detected"
    assert parse_sensor_data(0b00000010) == "No issues detected"
    assert parse_sensor_data(0b00000100) == "No issues detected"
    assert parse_sensor_data(0b00000000) == "Unknown value"
    assert parse_sensor_data(0b11111111) == "issues detected"

def test_check_inputs():
    result_l, result_r, result_b, l = check_inputs()
    assert result_l == "00000100"
    assert result_r == "00000100"
    assert result_b == "00000100"
    assert l == "00000100"

def test_check_sonsers_rst():
    result_F = check_sonsers_rst("00000100", "00000100", "00000100")
    assert result_F == "00000100"

def test_opera():
    a = opera(2)
    b = opera(4)
    c = opera(6)

    # Test the & operator
    assert (a & b).value == 0
    assert (b & c).value == 4

    # Test the | operator
    assert (a | b).value == 6
    assert (b | c).value == 6

    # Test the ^ operator
    assert (a ^ b).value == 6
    assert (b ^ c).value == 2

    # Test the << operator
    assert (a << b).value == 32
    assert (b << c).value == 384

    # Test the >> operator
    assert (a >> b).value == 0
    assert (c >> b).value == 1

    # Test the ~ operator
    assert (~a).value == -3
    assert (~b).value == -5



    
