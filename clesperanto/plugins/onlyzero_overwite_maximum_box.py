from ..core import execute

def onlyzero_overwrite_maximum_box (src, flag_dst, dst):

    parameters = {
        "dst": dst,
        "flag_dst": flag_dst,
        "src":src,
    }

    execute(__file__, 'onlyzero_overwrite_maximum_box_' + str(len(dst.shape)) + 'd_x.cl', 'onlyzero_overwrite_maximum_box_' + str(len(dst.shape)) + 'd', dst.shape, parameters)

    return [flag_dst, dst]
