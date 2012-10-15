# -*- encoding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 6
_modified_time = 1350183071.7842219
_template_filename='templates/root/index.mako'
_template_uri='root/index.mako'
_template_cache=cache.Cache(__name__, _modified_time)
_source_encoding='ascii'
_exports = ['init', 'left_panel', 'center_panel', 'late_javascripts', 'right_panel']


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    pass
def _mako_inherit(template, context):
    _mako_generate_namespaces(context)
    return runtime._inherit_from(context, u'/webapps/galaxy/base_panels.mako', _template_uri)
def render_body(context,**pageargs):
    context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        __M_writer = context.writer()
        # SOURCE LINE 1
        __M_writer(u'\n\n')
        # SOURCE LINE 75
        __M_writer(u'\n\n')
        # SOURCE LINE 91
        __M_writer(u'\n\n')
        # SOURCE LINE 105
        __M_writer(u'\n\n')
        # SOURCE LINE 125
        __M_writer(u'\n\n')
        # SOURCE LINE 139
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_init(context):
    context.caller_stack._push_frame()
    try:
        self = context.get('self', UNDEFINED)
        trans = context.get('trans', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 77
        __M_writer(u'\n')
        # SOURCE LINE 78

        self.has_left_panel = True
        self.has_right_panel = True
        self.active_view = "analysis"
        self.require_javascript = True
        
        
        # SOURCE LINE 83
        __M_writer(u'\n')
        # SOURCE LINE 84
        if trans.app.config.require_login and not trans.user:
            # SOURCE LINE 85
            __M_writer(u'    <script type="text/javascript">\n        if ( window != top ) {\n            top.location.href = location.href;\n        }\n    </script>\n')
            pass
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_left_panel(context):
    context.caller_stack._push_frame()
    try:
        h = context.get('h', UNDEFINED)
        n_ = context.get('n_', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 93
        __M_writer(u'\n    <div class="unified-panel-header" unselectable="on">\n        <div class=\'unified-panel-header-inner\'>\n')
        # SOURCE LINE 99
        __M_writer(u'            ')
        __M_writer(unicode(n_('Tools')))
        __M_writer(u'\n        </div>\n    </div>\n    <div class="unified-panel-body" style="overflow: hidden;">\n        <iframe name="galaxy_tools" id="galaxy_tools" src="')
        # SOURCE LINE 103
        __M_writer(unicode(h.url_for( controller='root', action='tool_menu' )))
        __M_writer(u'" frameborder="0" style="position: absolute; margin: 0; border: 0 none; height: 100%; width: 100%;"> </iframe>\n    </div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_center_panel(context):
    context.caller_stack._push_frame()
    try:
        tool_id = context.get('tool_id', UNDEFINED)
        m_c = context.get('m_c', UNDEFINED)
        h = context.get('h', UNDEFINED)
        m_a = context.get('m_a', UNDEFINED)
        workflow_id = context.get('workflow_id', UNDEFINED)
        trans = context.get('trans', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 107
        __M_writer(u'\n\n')
        # SOURCE LINE 110
        __M_writer(u'    ')

        if trans.app.config.require_login and not trans.user:
            center_url = h.url_for( controller='user', action='login' )
        elif tool_id is not None:
            center_url = h.url_for( 'tool_runner', tool_id=tool_id, from_noframe=True )
        elif workflow_id is not None:
            center_url = h.url_for( controller='workflow', action='run', id=workflow_id )
        elif m_c is not None:
            center_url = h.url_for( controller=m_c, action=m_a )
        else:
            center_url = h.url_for( '/static/welcome.html' )
        
        
        # SOURCE LINE 121
        __M_writer(u'\n    \n    <iframe name="galaxy_main" id="galaxy_main" frameborder="0" style="position: absolute; width: 100%; height: 100%;" src="')
        # SOURCE LINE 123
        __M_writer(unicode(center_url))
        __M_writer(u'"></iframe>\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_late_javascripts(context):
    context.caller_stack._push_frame()
    try:
        h = context.get('h', UNDEFINED)
        _ = context.get('_', UNDEFINED)
        parent = context.get('parent', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 3
        __M_writer(u'\n    ')
        # SOURCE LINE 4
        __M_writer(unicode(parent.late_javascripts()))
        __M_writer(u'\n    <script type="text/javascript">\n    // Set up GalaxyAsync object.\n    var galaxy_async = new GalaxyAsync();\n    galaxy_async.set_func_url(galaxy_async.set_user_pref, "')
        # SOURCE LINE 8
        __M_writer(unicode(h.url_for( controller='user', action='set_user_pref_async' )))
        __M_writer(u'");\n    \n    $(function(){\n        // Init history options.\n        $("#history-options-button").css( "position", "relative" );\n        make_popupmenu( $("#history-options-button"), {\n            "')
        # SOURCE LINE 14
        __M_writer(unicode(_("History Lists")))
        __M_writer(u'": null,\n            "')
        # SOURCE LINE 15
        __M_writer(unicode(_("Saved Histories")))
        __M_writer(u'": function() {\n                galaxy_main.location = "')
        # SOURCE LINE 16
        __M_writer(unicode(h.url_for( controller='history', action='list')))
        __M_writer(u'";\n            },\n            "')
        # SOURCE LINE 18
        __M_writer(unicode(_("Histories Shared with Me")))
        __M_writer(u'": function() {\n                galaxy_main.location = "')
        # SOURCE LINE 19
        __M_writer(unicode(h.url_for( controller='history', action='list_shared')))
        __M_writer(u'";\n            },\n            "')
        # SOURCE LINE 21
        __M_writer(unicode(_("Current History")))
        __M_writer(u'": null,\n            "')
        # SOURCE LINE 22
        __M_writer(unicode(_("Create New")))
        __M_writer(u'": function() {\n                galaxy_history.location = "')
        # SOURCE LINE 23
        __M_writer(unicode(h.url_for( controller='root', action='history_new' )))
        __M_writer(u'";\n            },\n            "')
        # SOURCE LINE 25
        __M_writer(unicode(_("Clone")))
        __M_writer(u'": function() {\n                galaxy_main.location = "')
        # SOURCE LINE 26
        __M_writer(unicode(h.url_for( controller='history', action='clone')))
        __M_writer(u'";\n            },\n            "')
        # SOURCE LINE 28
        __M_writer(unicode(_("Copy Datasets")))
        __M_writer(u'": function() {\n                galaxy_main.location = "')
        # SOURCE LINE 29
        __M_writer(unicode(h.url_for( controller='dataset', action='copy_datasets' )))
        __M_writer(u'";\n            },\n            "')
        # SOURCE LINE 31
        __M_writer(unicode(_("Share or Publish")))
        __M_writer(u'": function() {\n                galaxy_main.location = "')
        # SOURCE LINE 32
        __M_writer(unicode(h.url_for( controller='history', action='sharing' )))
        __M_writer(u'";\n            },\n            "')
        # SOURCE LINE 34
        __M_writer(unicode(_("Extract Workflow")))
        __M_writer(u'": function() {\n                galaxy_main.location = "')
        # SOURCE LINE 35
        __M_writer(unicode(h.url_for( controller='workflow', action='build_from_current_history' )))
        __M_writer(u'";\n            },\n            "')
        # SOURCE LINE 37
        __M_writer(unicode(_("Dataset Security")))
        __M_writer(u'": function() {\n                galaxy_main.location = "')
        # SOURCE LINE 38
        __M_writer(unicode(h.url_for( controller='root', action='history_set_default_permissions' )))
        __M_writer(u'";\n            },\n            "')
        # SOURCE LINE 40
        __M_writer(unicode(_("Show Deleted Datasets")))
        __M_writer(u'": function() {\n                galaxy_history.location = "')
        # SOURCE LINE 41
        __M_writer(unicode(h.url_for( controller='root', action='history', show_deleted=True)))
        __M_writer(u'";\n            },\n            "')
        # SOURCE LINE 43
        __M_writer(unicode(_("Show Hidden Datasets")))
        __M_writer(u'": function() {\n                galaxy_history.location = "')
        # SOURCE LINE 44
        __M_writer(unicode(h.url_for( controller='root', action='history', show_hidden=True)))
        __M_writer(u'";\n            },\n            "')
        # SOURCE LINE 46
        __M_writer(unicode(_("Purge Deleted Datasets")))
        __M_writer(u'": function() {\n                if ( confirm( "Really delete all deleted datasets permanently? This cannot be undone." ) ) {\n                    galaxy_main.location = "')
        # SOURCE LINE 48
        __M_writer(unicode(h.url_for( controller='history', action='purge_deleted_datasets' )))
        __M_writer(u'";\n                }\n            },\n            "')
        # SOURCE LINE 51
        __M_writer(unicode(_("Show Structure")))
        __M_writer(u'": function() {\n                galaxy_main.location = "')
        # SOURCE LINE 52
        __M_writer(unicode(h.url_for( controller='history', action='display_structured' )))
        __M_writer(u'";\n            },\n            "')
        # SOURCE LINE 54
        __M_writer(unicode(_("Export to File")))
        __M_writer(u'": function() {\n                galaxy_main.location = "')
        # SOURCE LINE 55
        __M_writer(unicode(h.url_for( controller='history', action='export_archive' )))
        __M_writer(u'";\n            },\n            "')
        # SOURCE LINE 57
        __M_writer(unicode(_("Delete")))
        __M_writer(u'": function() {\n                if ( confirm( "Really delete the current history?" ) ) {\n                    galaxy_main.location = "')
        # SOURCE LINE 59
        __M_writer(unicode(h.url_for( controller='history', action='delete_current' )))
        __M_writer(u'";\n                }\n            },\n            "')
        # SOURCE LINE 62
        __M_writer(unicode(_("Delete Permanently")))
        __M_writer(u'": function() {\n                if ( confirm( "Really delete the current history permanently? This cannot be undone." ) ) {\n                    galaxy_main.location = "')
        # SOURCE LINE 64
        __M_writer(unicode(h.url_for( controller='history', action='delete_current', purge=True )))
        __M_writer(u'";\n                }\n            },\n            "')
        # SOURCE LINE 67
        __M_writer(unicode(_("Other Actions")))
        __M_writer(u'": null,\n            "')
        # SOURCE LINE 68
        __M_writer(unicode(_("Import from File")))
        __M_writer(u'": function() {\n                galaxy_main.location = "')
        # SOURCE LINE 69
        __M_writer(unicode(h.url_for( controller='history', action='import_archive' )))
        __M_writer(u'";\n            }\n        });\n        \n    });\n    </script>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_right_panel(context):
    context.caller_stack._push_frame()
    try:
        h = context.get('h', UNDEFINED)
        _ = context.get('_', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 127
        __M_writer(u'\n    <div class="unified-panel-header" unselectable="on">\n        <div class="unified-panel-header-inner">\n            <div style="float: right">\n                <a id="history-options-button" class=\'panel-header-button\' href="')
        # SOURCE LINE 131
        __M_writer(unicode(h.url_for( controller='root', action='history_options' )))
        __M_writer(u'" target="galaxy_main"><span class="ficon large cog"></span></a>\n            </div>\n            <div class="panel-header-text">')
        # SOURCE LINE 133
        __M_writer(unicode(_('History')))
        __M_writer(u'</div>\n        </div>\n    </div>\n    <div class="unified-panel-body" style="overflow: hidden;">\n        <iframe name="galaxy_history" width="100%" height="100%" frameborder="0" style="position: absolute; margin: 0; border: 0 none; height: 100%;" src="')
        # SOURCE LINE 137
        __M_writer(unicode(h.url_for( controller='root', action='history' )))
        __M_writer(u'"></iframe>\n    </div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


