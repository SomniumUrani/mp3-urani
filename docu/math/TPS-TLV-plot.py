import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(1, 10, 50)
#units 1       500
tps = [1.3619, 0.8359]
tlv = [0.2347, 0.1391]

tlva = (tps[0] + tlv[0]) * x + (3 / x)
tpsa = tps[0]*2 * x + (3 / x)

tlvb = (tps[0] + tlv[0]) * x + (3 / x)
tpsb = tps[0]*2 * x + (3 / x)

fig = plt.figure(figsize=(8, 8))
plt.subplot(2, 1, 1)

plt.plot(x, tlva, label="With TLV")
plt.plot(x, tpsa, label="TPS only")
plt.title("1 unit price")
plt.ylabel("Price in USD")

plt.grid(True)
plt.legend()

plt.subplot(2, 1, 2)
plt.plot(x, tlvb, label="With TLV")
plt.plot(x, tpsb, label="TPS only")
plt.title("500 units price")
plt.ylabel("Price in USD")

plt.grid(True)
plt.legend()


print("Show? N/y")
if input().lower() == "y":
    plt.show()

print("Save? N/y")
if input().lower() == "y":
    fig.savefig("TPS-TLV.png")
