import planckStyle as s

g=s.plotter

labels=[s.planck,s.lensing,s.WP,s.WPhighL]
roots=['base_planck_CAMspec_lowl','base_planck_CAMspec_lowl_post_lensing','base_planck_CAMspec_lowl_lowLike','base_planck_CAMspec_lowl_lowLike_highL']
g.plots_1d(roots, legend_labels=labels)
g.export('outputs/planck_datasets_1d.eps')

g.newPlot()
g.plots_1d(roots,['omegabh2','omegach2','tau','A','ns','omegam','H0','sigma8'],nx=2, legend_labels=labels)
g.export('outputs/planck_datasets_1d_params.eps')


g.newPlot()
labels=[s.planck,s.lensing,s.WP]
roots=['base_planck_CAMspec_lowl','base_planck_CAMspec_lowl_post_lensing','base_planck_CAMspec_lowl_lowLike']

g.plots_1d(roots,['tau','zrei','A','sigma8'],nx=2, legend_labels=labels)
g.export('outputs/reion_tau_1D.eps')
