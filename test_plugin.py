import sys
from pathlib import Path


ROOT = Path(__file__).parent

sys.path.insert(0, str(ROOT))


from plugins.hardware.plugin import HardwarePlugin



plugin = HardwarePlugin()


print("====================")
print("PLUGIN TEST")
print("====================")


print(plugin.start())


print()


dados = plugin.info()


for chave, valor in dados.items():

    print(
        chave,
        ":",
        valor
    )


print()

print(plugin.stop())