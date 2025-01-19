import numpy as np
import matplotlib.pyplot as plt

MU_0 = 4 * np.pi * 1e-7  # Permeability of free space (H/m)
conductivities = [0.01,0.1, 0.01] # (S/m)
thicknesses =  [100, 200] # m
frequency = 10# Hz

def calculate_impedance(frequency, conductivities, thicknesses):
    MU_0 = 4 * np.pi * 1e-7  # Magnetic permeability of free space
    omega = 2 * np.pi * frequency
    Z_next = np.sqrt(1j * omega * MU_0 / conductivities[-1])  # Bottom-most layer

    for i in range(len(conductivities) - 2, -1, -1):
        gamma = np.sqrt(1j * omega * MU_0 * conductivities[i])
        R = np.sqrt(1j * omega * MU_0 / conductivities[i])
        Z_next = R * (Z_next + R * np.tanh(gamma * thicknesses[i])) / (R + Z_next * np.tanh(gamma * thicknesses[i]))

    return Z_next

def calculate_apparent_resistivity(frequency, conductivities, thicknesses):
    Z0 = calculate_impedance(frequency, conductivities, thicknesses)
    omega = 2 * np.pi * frequency
    rho_a = abs(Z0)**2 / (MU_0 * omega)
    phi = np.angle(Z0, deg=True)  # Phase in degrees
    return rho_a, phi

rho_a, phi = calculate_apparent_resistivity(frequency, conductivities, thicknesses)
delta = 500 / np.sqrt(frequency / rho_a)

print("Skin Depth = {a} \n Apparent Resistivity = {b}".format(a = delta, b = rho_a))

Frequencies = np.logspace(-2, 4, 100) 
freq_nom = np.linspace(10, 100, 10)

rhos = []
phis = []

for i in Frequencies:
    rho_a, phi = calculate_apparent_resistivity(i, conductivities, thicknesses)
    rhos.append(rho_a)
    phis.append(phi)

rho_a, phi = calculate_apparent_resistivity(frequency, conductivities, thicknesses)

fig, ax1 = plt.subplots()
ax1.set_xlabel("Frequency (Hz)")
ax1.set_xscale("log")
ax1.set_ylabel("Apparent Resistivity (Ohm·m)", color="tab:blue")
ax1.plot(Frequencies, rhos, color="tab:blue", label="Apparent Resistivity")
ax1.scatter([frequency], [rho_a], color="red", label= str(frequency) + "Hz Point")
ax1.tick_params(axis="y", labelcolor="tab:blue")
ax1.grid(True, which="both", linestyle="--", linewidth=0.5)
ax2 = ax1.twinx()
ax2.set_ylabel("Phase (degrees)", color="orange")
ax2.plot(Frequencies, phis, color="orange", label="Phase")
ax2.tick_params(axis="y", labelcolor="tab:orange")
fig.tight_layout()
plt.title("MT Response: Apparent Resistivity and Phase")
ax1.legend()
ax2.legend()

plt.show()

frequency_range = freq_nom # Frequencies from 10 Hz to 100 Hz
apparent_resistivity = rho_a  # Ohm·m
omega_range = 2 * np.pi * frequency_range  # Angular frequency (rad/s)


f_upper = 100 #Hz
f_lower = 10 

max_f = []
min_f = []

for i in Frequencies:
    max_f.append((abs(100 - i), i))
    min_f.append((abs(10 - i), i))

max_f_index = list(Frequencies).index(min(max_f)[1])
min_f_index = list(Frequencies).index(min(min_f)[1])

phis_between = phis[min_f_index:max_f_index+1]

phase_range = np.linspace(min(phis_between), max(phis_between), len(freq_nom))  # Assumed phase range in degrees

# Calculate Bostick resistivity
log_omega = np.log(omega_range)
dphi_dln_omega = np.gradient(phase_range, log_omega)  # Derivative of phase w.r.t ln(omega)

# Convert degrees to radians for dphi/dln(omega)
dphi_dln_omega_rad = dphi_dln_omega * (np.pi / 180)

# Bostick resistivity formula
bostick_resistivity = apparent_resistivity / (1 + dphi_dln_omega_rad**2)

av_rho = (rhos[min_f_index: max_f_index][0] + rhos[min_f_index: max_f_index][-1]) / 2

print("Skin Depth = {a:<20}\nApparent Res. = {b:<20}\nFreq. Range Res. = {c:<20} \
      ".format(a = round(delta, 2), b = round(rho_a, 2), c = round(av_rho,2 )))

