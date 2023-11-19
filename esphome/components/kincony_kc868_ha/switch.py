import esphome.codegen as cg
import esphome.config_validation as cv
from esphome.components import switch
from esphome.const import CONF_ID
from . import (
    KinconyKc868Ha,
    CONF_KINCONY_KC868_HA_ID,
    CONF_BIND_OUTPUT,
)

DEPENDENCIES = ['kincony_kc868_ha']

kincony_kc868_ha_ns = cg.esphome_ns.namespace('kincony_kc868_ha')
KinconyKc868HaSwitch = kincony_kc868_ha_ns.class_('KinconyKc868HaSwitch', switch.Switch)

CONFIG_SCHEMA = switch.SWITCH_SCHEMA.extend({
    cv.GenerateID(): cv.declare_id(KinconyKc868HaSwitch),
    cv.GenerateID(CONF_KINCONY_KC868_HA_ID): cv.use_id(KinconyKc868Ha),
    cv.Required(CONF_BIND_OUTPUT): cv.int_range(min=1, max=128),
}).extend(cv.COMPONENT_SCHEMA)

def to_code(config):
    paren = yield cg.get_variable(config[KC868_HA_ID])
    var = cg.new_Pvariable(config[CONF_ID])
    yield switch.register_switch(var, config)
    cg.add(var.set_target_relay_controller_addr(paren.get_target_relay_controller_addr()))
    cg.add(var.set_switch_adapter_addr(paren.get_switch_adapter_addr()))
    cg.add(var.set_bind_output(config[CONF_BIND_OUTPUT]))
    cg.add(paren.register_switch(var))
