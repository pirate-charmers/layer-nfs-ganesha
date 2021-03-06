from charms.reactive import when_not, set_state, hook
from charmhelpers.core.hookenv import application_version_set
from charms import layer


@when_not('layer-version.installed')
def install_layer_version():
    with open(layer.options('version')['file_name'], 'r') as version:
        application_version_set(version.readline().strip())
    set_state('layer-version.installed')


@hook('upgrade-charm')
def update_version():
    with open(layer.options('version')['file_name'], 'r') as version:
        application_version_set(version.readline().strip())
