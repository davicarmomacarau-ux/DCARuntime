from plugins.security.plugin import SecurityPlugin


plugin = SecurityPlugin()


print("====================")
print("SECURITY TEST")
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