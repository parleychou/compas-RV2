from __future__ import print_function
from __future__ import absolute_import
from __future__ import division

import compas_rhino
from compas_rv2.rhino import get_scene
from compas.utilities import flatten


__commandname__ = "RV2form_modify_edges"


def RunCommand(is_interactive):

    scene = get_scene()
    if not scene:
        return

    form = scene.get("form")[0]
    if not form:
        return

    options = ['Continuous', 'Parallel', 'Manual']
    option = compas_rhino.rs.GetString("Selection Type.", options[-1], options)

    if option == 'Continuous':
        temp = form.select_edges()
        keys = list(set(flatten([form.datastructure.continuous_edges(key) for key in temp])))

    elif option == 'Parallel':
        temp = form.select_edges()
        keys = list(set(flatten([form.datastructure.parallel_edges(key) for key in temp])))

    else:
        keys = form.select_edges()

    if keys:
        public = [name for name in form.datastructure.default_edge_attributes.keys() if not name.startswith('_')]
        if form.update_edges_attributes(keys, names=public):
            scene.update()


# ==============================================================================
# Main
# ==============================================================================

if __name__ == "__main__":

    RunCommand(True)
