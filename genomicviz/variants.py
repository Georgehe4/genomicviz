import ipywidgets as widgets
from traitlets import Unicode, Int

@widgets.register('genomicviz.Variants')
class Variants(widgets.DOMWidget):
    """"""
    _view_name = Unicode('VariantView').tag(sync=True)
    _model_name = Unicode('VariantModel').tag(sync=True)
    _view_module = Unicode('genomic-viz').tag(sync=True)
    _model_module = Unicode('genomic-viz').tag(sync=True)
    _view_module_version = Unicode('^0.1.0').tag(sync=True)
    _model_module_version = Unicode('^0.1.0').tag(sync=True)
    json = Unicode('{}').tag(sync=True)
    build = Unicode('hg19').tag(sync=True)
    contig = Unicode('chr1').tag(sync=True)
    start = Int(1).tag(sync=True)
    stop = Int(50).tag(sync=True)
