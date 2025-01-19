# EM-Analysis
This project provides Python scripts for modeling and analyzing magnetotelluric (MT) responses in the context of geophysics in order to understand the electromagnetic properties of the Earth's subsurface.

Features

    -  Impedance Calculation: The script models the impedance of the Earth's subsurface using a multi-layer model, which can have different conductivities and thicknesses for each layer. The impedance is computed across a user-defined range of frequencies.
    -   Apparent Resistivity and Phase: It calculates the apparent resistivity and phase for each frequency, which are key outputs for interpreting magnetotelluric (MT) survey data.
    -  Skin Depth Calculation: The skin depth is computed for each layer, which indicates the penetration depth of electromagnetic waves in a conductive medium.
    -  Bostick Resistivity: Implements the Bostick resistivity model using the phase derivative with respect to angular frequency, a technique used in MT data inversion.
    -  Multi-layer Subsurface Models: The script is designed to handle multiple layers of the Earth's subsurface, each with its own conductivity and thickness.
    -  Interactive Visualizations: The results, including apparent resistivity and phase, are plotted over a frequency range with dual axes for better understanding. A subsurface model of conductivity and thickness is also plotted.
