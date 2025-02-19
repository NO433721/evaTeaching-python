import utils

import matplotlib.pyplot as plt 

plt.figure(figsize=(14,10))
fit_functions = ['f01', 'f02', 'f06', 'f08', 'f10']
for idx, fit_fn in enumerate(fit_functions):
    plt.subplot(2, 3, idx+1)
    utils.plot_experiments(
        'continuous', [f'default.{fit_fn}', 
                       f'adaptive.{fit_fn}'])
    plt.yscale("log")
    plt.title(f"{fit_fn}", fontname="DejaVu Sans Bold")
# utils.plot_experiments("continuous", ["default", "adaptive_mutation"])
plt.yscale("log")
plt.tight_layout()
plt.savefig("continuous_adaptive.jpg")
plt.show()