# EM-Analysis
This project provides Python scripts for modeling and analyzing magnetotelluric (MT) responses in the context of geophysics in order to understand the electromagnetic properties of the Earth's subsurface.

Features
    -  Impedance Calculation: The script models the impedance of the Earth's subsurface using a multi-layer model, which can have different conductivities and thicknesses for each layer. The impedance is computed across a user-defined range of frequencies.
    -  Apparent Resistivity and Phase: It calculates the apparent resistivity and phase for each frequency, which are key outputs for interpreting magnetotelluric (MT) survey data.
    -  Skin Depth Calculation: The skin depth is computed for each layer, which indicates the penetration depth of electromagnetic waves in a conductive medium.
    -  Bostick Resistivity: Implements the Bostick resistivity model using the phase derivative with respect to angular frequency, a technique used in MT data inversion.
    -  Multi-layer Subsurface Models: The script is designed to handle multiple layers of the Earth's subsurface, each with its own conductivity and thickness.
    -  Interactive Visualizations: The results, including apparent resistivity and phase, are plotted over a frequency range with dual axes for better understanding. A subsurface model of conductivity and thickness is also plotted.

Inputs
    -    Frequency: A list of frequencies (in Hz) at which to compute the impedance and resistivity. This can either be a single frequency or a range of frequencies.
    -    Conductivities: A list of conductivities (in S/m) for each layer in the subsurface. These values represent the electrical conductivity of each geological layer.
    -    Thicknesses: A list of thicknesses (in meters) for each layer in the subsurface. Each value corresponds to the depth of the respective layer.
    -    Frequency Range: An optional log-spaced frequency range for plotting the resistivity and phase response across different frequencies.
    
Outputs
    -    Apparent Resistivity: The apparent resistivity (in Ohm·m) as a function of frequency.
    -    Phase: The phase (in degrees) as a function of frequency, which describes the phase shift of the electromagnetic wave as it travels through the Earth’s layers.
    -    Skin Depth: The skin depth (in meters) indicating how deep electromagnetic waves can penetrate into the Earth.
    Visualizations:
        A plot of apparent resistivity versus frequency.
        A plot of phase versus frequency.
        Subsurface conductivity and thickness profile.

![rho_freq_phase](https://github.com/user-attachments/assets/d4c05e78-4dd4-4bc2-b5fa-bc2847216c69)


![cross_section-ex](https://github.com/user-attachments/assets/706ac9d0-e0de-4ec2-b8d3-a5f39b641fb3)
