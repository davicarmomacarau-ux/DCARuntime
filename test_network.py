from plugins.network.plugin import NetworkPlugin


plugin = NetworkPlugin()


print("====================")
print("NETWORK TEST")
print("====================")


print(plugin.start())


print()


for chave, valor in plugin.info().items():

    print(
        chave,
        ":",
        valor
    )


print()

print(plugin.stop())