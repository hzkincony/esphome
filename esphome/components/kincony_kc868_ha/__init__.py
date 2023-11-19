import esphome.codegen as cg
import esphome.config_validation as cv
from esphome.const import (
    CONF_ID,
    CONF_UART_ID
)
from esphome.components import uart

CODEOWNERS = ["@hzkincony"]
DEPENDENCIES = ["uart"]
AUTO_LOAD = ['binary_sensor', 'switch']
MULTI_CONF = True

CONF_KINCONY_KC868_HA_ID = 'kincony_kc868_ha_id'
CONF_TARGET_RELAY_CONTROLLER_ADDR = "target_relay_controller_addr"
CONF_SWITCH_ADAPTER_ADDR = "switch_adapter_addr"
CONF_BIND_OUTPUT = "bind_output"

kincony_kc868_ha_ns = cg.esphome_ns.namespace('kincony_kc868_ha')

KinconyKc868Ha = kincony_kc868_ha_ns.class_('KinconyKc868Ha', cg.Component, uart.UARTDevice)

CONFIG_SCHEMA = cv.Schema({
    cv.GenerateID(): cv.declare_id(KinconyKc868Ha),
    cv.Optional(CONF_TARGET_RELAY_CONTROLLER_ADDR, default=1): cv.int_range(min=1, max=128),
    cv.Optional(CONF_SWITCH_ADAPTER_ADDR, default=10): cv.int_range(min=10, max=99),
}).extend(uart.UART_DEVICE_SCHEMA).extend(cv.COMPONENT_SCHEMA)

def to_code(config):
    u = yield cg.get_variable(config[CONF_UART_ID])
    var = cg.new_Pvariable(config[CONF_ID], u)
    yield cg.register_component(var, config)
    cg.add(var.set_target_relay_controller_addr(config[CONF_TARGET_RELAY_CONTROLLER_ADDR]))
    cg.add(var.set_switch_adapter_addr(config[CONF_SWITCH_ADAPTER_ADDR]))
    yield uart.register_uart_device(var, config)
