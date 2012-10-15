# -*- encoding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 6
_modified_time = 1350183676.9206631
_template_filename=u'templates/root/history_common.mako'
_template_uri=u'root/history_common.mako'
_template_cache=cache.Cache(__name__, _modified_time)
_source_encoding='ascii'
_exports = ['render_download_links', 'render_dataset']


def render_body(context,**pageargs):
    context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        n_ = context.get('n_', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 1
        _=n_ 
        
        __M_locals_builtin_stored = __M_locals_builtin()
        __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['_'] if __M_key in __M_locals_builtin_stored]))
        __M_writer(u'\n\n')
        # SOURCE LINE 27
        __M_writer(u'\n\n')
        # SOURCE LINE 338
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_render_download_links(context,data,dataset_id):
    context.caller_stack._push_frame()
    try:
        h = context.get('h', UNDEFINED)
        isinstance = context.get('isinstance', UNDEFINED)
        _ = context.get('_', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 3
        __M_writer(u'\n    ')
        # SOURCE LINE 4

        from galaxy.datatypes.metadata import FileParameter
            
        
        # SOURCE LINE 6
        __M_writer(u'\n')
        # SOURCE LINE 7
        if not data.purged:
            # SOURCE LINE 9
            __M_writer(u'        ')
            meta_files = [ k for k in data.metadata.spec.keys() if isinstance( data.metadata.spec[k].param, FileParameter ) ] 
            
            __M_writer(u'\n')
            # SOURCE LINE 10
            if meta_files:
                # SOURCE LINE 11
                __M_writer(u'            <div popupmenu="dataset-')
                __M_writer(unicode(dataset_id))
                __M_writer(u'-popup">\n                <a class="action-button" href="')
                # SOURCE LINE 12
                __M_writer(unicode(h.url_for( controller='dataset', action='display', dataset_id=dataset_id, \
                    to_ext=data.ext )))
                # SOURCE LINE 13
                __M_writer(u'">Download Dataset</a>\n                <a>Additional Files</a>\n')
                # SOURCE LINE 15
                for file_type in meta_files:
                    # SOURCE LINE 16
                    __M_writer(u'                <a class="action-button" href="')
                    __M_writer(unicode(h.url_for( controller='/dataset', action='get_metadata_file', \
                    hda_id=dataset_id, metadata_name=file_type )))
                    # SOURCE LINE 17
                    __M_writer(u'">Download ')
                    __M_writer(unicode(file_type))
                    __M_writer(u'</a>\n')
                    pass
                # SOURCE LINE 19
                __M_writer(u'            </div>\n            <div style="float:left;" class="menubutton split popup" id="dataset-')
                # SOURCE LINE 20
                __M_writer(unicode(dataset_id))
                __M_writer(u'-popup">\n')
                pass
            # SOURCE LINE 22
            __M_writer(u'        <a href="')
            __M_writer(unicode(h.url_for( controller='/dataset', action='display', dataset_id=dataset_id, to_ext=data.ext )))
            __M_writer(u'" title=\'')
            __M_writer(unicode(_("Download")))
            __M_writer(u'\' class="icon-button disk tooltip"></a>\n')
            # SOURCE LINE 23
            if meta_files:
                # SOURCE LINE 24
                __M_writer(u'            </div>\n')
                pass
            pass
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_render_dataset(context,data,hid,show_deleted_on_refresh=False,for_editing=True,display_structured=False):
    context.caller_stack._push_frame()
    try:
        isinstance = context.get('isinstance', UNDEFINED)
        def render_download_links(data,dataset_id):
            return render_render_download_links(context,data,dataset_id)
        h = context.get('h', UNDEFINED)
        app = context.get('app', UNDEFINED)
        enumerate = context.get('enumerate', UNDEFINED)
        request = context.get('request', UNDEFINED)
        len = context.get('len', UNDEFINED)
        def render_dataset(data,hid,show_deleted_on_refresh=False,for_editing=True,display_structured=False):
            return render_render_dataset(context,data,hid,show_deleted_on_refresh,for_editing,display_structured)
        trans = context.get('trans', UNDEFINED)
        _ = context.get('_', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 30
        __M_writer(u'\n    ')
        # SOURCE LINE 31


        from galaxy.datatypes.xml import Phyloxml
        from galaxy.datatypes.data import Newick, Nexus
        dataset_id = trans.security.encode_id( data.id )
        
        if data.state in ['no state','',None]:
            data_state = "queued"
        else:
            data_state = data.state
        current_user_roles = trans.get_current_user_roles()
        can_edit = not ( data.deleted or data.purged )
            
        
        # SOURCE LINE 43
        __M_writer(u'\n')
        # SOURCE LINE 44
        if not trans.user_is_admin() and not trans.app.security_agent.can_access_dataset( current_user_roles, data.dataset ):
            # SOURCE LINE 45
            __M_writer(u'        <div class="historyItemWrapper historyItem historyItem-')
            __M_writer(unicode(data_state))
            __M_writer(u' historyItem-noPermission" id="historyItem-')
            __M_writer(unicode(dataset_id))
            __M_writer(u'">\n')
            # SOURCE LINE 46
        else:
            # SOURCE LINE 47
            __M_writer(u'        <div class="historyItemWrapper historyItem historyItem-')
            __M_writer(unicode(data_state))
            __M_writer(u'" id="historyItem-')
            __M_writer(unicode(dataset_id))
            __M_writer(u'">\n')
            pass
        # SOURCE LINE 49
        __M_writer(u'        \n')
        # SOURCE LINE 50
        if data.deleted or data.purged or data.dataset.purged:
            # SOURCE LINE 51
            __M_writer(u'        <div class="warningmessagesmall"><strong>\n')
            # SOURCE LINE 52
            if data.dataset.purged or data.purged:
                # SOURCE LINE 53
                __M_writer(u'                This dataset has been deleted and removed from disk.\n')
                # SOURCE LINE 54
            else:
                # SOURCE LINE 55
                __M_writer(u'                This dataset has been deleted. \n')
                # SOURCE LINE 56
                if for_editing:
                    # SOURCE LINE 57
                    __M_writer(u'                    Click <a href="')
                    __M_writer(unicode(h.url_for( controller='dataset', action='undelete', dataset_id=dataset_id )))
                    __M_writer(u'" class="historyItemUndelete" id="historyItemUndeleter-')
                    __M_writer(unicode(dataset_id))
                    __M_writer(u'" target="galaxy_history">here</a> to undelete\n')
                    # SOURCE LINE 58
                    if trans.app.config.allow_user_dataset_purge:
                        # SOURCE LINE 59
                        __M_writer(u'                        or <a href="')
                        __M_writer(unicode(h.url_for( controller='dataset', action='purge', dataset_id=dataset_id )))
                        __M_writer(u'" class="historyItemPurge" id="historyItemPurger-')
                        __M_writer(unicode(dataset_id))
                        __M_writer(u'" target="galaxy_history">here</a> to immediately remove it from disk.\n')
                        # SOURCE LINE 60
                    else:
                        # SOURCE LINE 61
                        __M_writer(u'                        it.\n')
                        pass
                    pass
                pass
            # SOURCE LINE 65
            __M_writer(u'        </strong></div>\n')
            pass
        # SOURCE LINE 67
        __M_writer(u'\n')
        # SOURCE LINE 68
        if data.visible is False:
            # SOURCE LINE 69
            __M_writer(u'        <div class="warningmessagesmall">\n            <strong>This dataset has been hidden. Click <a href="')
            # SOURCE LINE 70
            __M_writer(unicode(h.url_for( controller='dataset', action='unhide', dataset_id=dataset_id )))
            __M_writer(u'" class="historyItemUnhide" id="historyItemUnhider-')
            __M_writer(unicode(dataset_id))
            __M_writer(u'" target="galaxy_history">here</a> to unhide.</strong>\n        </div>\n')
            pass
        # SOURCE LINE 73
        __M_writer(u'\n')
        # SOURCE LINE 75
        __M_writer(u'    <div style="overflow: hidden;" class="historyItemTitleBar">     \n        <div class="historyItemButtons">\n')
        # SOURCE LINE 77
        if data_state == "upload":
            # SOURCE LINE 81
            __M_writer(u"                <span title='")
            __M_writer(unicode(_("Display Data")))
            __M_writer(u"' class='icon-button display_disabled tooltip'></span>\n")
            # SOURCE LINE 82
            if for_editing:
                # SOURCE LINE 83
                __M_writer(u"                    <span title='Edit Attributes' class='icon-button edit_disabled tooltip'></span>\n")
                pass
            # SOURCE LINE 85
        else:
            # SOURCE LINE 86
            __M_writer(u'                ')
 
            if for_editing:
                display_url = h.url_for( controller='dataset', action='display', dataset_id=dataset_id, preview=True, filename='' )
            else:
                # Get URL for display only.
                if data.history.user and data.history.user.username:
                    display_url = h.url_for( controller='dataset', action='display_by_username_and_slug',
                                             username=data.history.user.username, slug=dataset_id, filename='' )
                else:
                    # HACK: revert to for_editing display URL when there is no user/username. This should only happen when
                    # there's no user/username because dataset is being displayed by history/view after error reported.
                    # There are no security concerns here because both dataset/display and dataset/display_by_username_and_slug
                    # check user permissions (to the same degree) before displaying.
                    display_url = h.url_for( controller='dataset', action='display', dataset_id=dataset_id, preview=True, filename='' )
                            
            
            # SOURCE LINE 100
            __M_writer(u'\n')
            # SOURCE LINE 101
            if data.purged:
                # SOURCE LINE 102
                __M_writer(u'                    <span class="icon-button display_disabled tooltip" title="Cannot display datasets removed from disk"></span>\n')
                # SOURCE LINE 103
            else:
                # SOURCE LINE 104
                __M_writer(u'                    <a class="icon-button display tooltip" dataset_id="')
                __M_writer(unicode(dataset_id))
                __M_writer(u'" title=\'')
                __M_writer(unicode(_("Display data in browser")))
                __M_writer(u'\' href="')
                __M_writer(unicode(display_url))
                __M_writer(u'"\n')
                # SOURCE LINE 105
                if for_editing:
                    # SOURCE LINE 106
                    __M_writer(u'                        target="galaxy_main"\n')
                    pass
                # SOURCE LINE 108
                __M_writer(u'                    ></a>\n')
                pass
            # SOURCE LINE 110
            __M_writer(u'                \n')
            # SOURCE LINE 112
            if for_editing:
                # SOURCE LINE 113
                if data.deleted and not data.purged:
                    # SOURCE LINE 114
                    __M_writer(u'                        <span title="Undelete dataset to edit attributes" class="icon-button edit_disabled tooltip"></span>\n')
                    # SOURCE LINE 115
                elif data.purged:
                    # SOURCE LINE 116
                    __M_writer(u'                        <span title="Cannot edit attributes of datasets removed from disk" class="icon-button edit_disabled tooltip"></span>\n')
                    # SOURCE LINE 117
                else:
                    # SOURCE LINE 118
                    __M_writer(u'                        <a class="icon-button edit tooltip" title=\'')
                    __M_writer(unicode(_("Edit attributes")))
                    __M_writer(u'\' href="')
                    __M_writer(unicode(h.url_for( controller='dataset', action='edit', dataset_id=dataset_id )))
                    __M_writer(u'" target="galaxy_main"></a>\n')
                    pass
                pass
            # SOURCE LINE 121
            __M_writer(u'                \n')
            pass
        # SOURCE LINE 123
        __M_writer(u'            \n')
        # SOURCE LINE 125
        if for_editing:
            # SOURCE LINE 126
            if can_edit:
                # SOURCE LINE 127
                __M_writer(u'                    <a class="icon-button delete tooltip" title=\'')
                __M_writer(unicode(_("Delete")))
                __M_writer(u'\' href="')
                __M_writer(unicode(h.url_for( controller='dataset', action='delete', dataset_id=dataset_id, show_deleted_on_refresh=show_deleted_on_refresh )))
                __M_writer(u'" id="historyItemDeleter-')
                __M_writer(unicode(dataset_id))
                __M_writer(u'"></a>\n')
                # SOURCE LINE 128
            else:
                # SOURCE LINE 129
                __M_writer(u'                    <span title="Dataset is already deleted" class="icon-button delete_disabled tooltip"></span>\n')
                pass
            pass
        # SOURCE LINE 132
        __M_writer(u'        </div>\n        <span class="state-icon"></span>\n        <span class="historyItemTitle">')
        # SOURCE LINE 134
        __M_writer(unicode(hid))
        __M_writer(u': ')
        __M_writer(unicode(data.display_name()))
        __M_writer(u'</span>\n    </div>\n        \n')
        # SOURCE LINE 138
        __M_writer(u'    \n    <div id="info')
        # SOURCE LINE 139
        __M_writer(unicode(data.id))
        __M_writer(u'" class="historyItemBody">\n')
        # SOURCE LINE 140
        if not trans.user_is_admin() and not trans.app.security_agent.can_access_dataset( current_user_roles, data.dataset ):
            # SOURCE LINE 141
            __M_writer(u'            <div>You do not have permission to view this dataset.</div>\n')
            # SOURCE LINE 142
        elif data_state == "upload":
            # SOURCE LINE 143
            __M_writer(u'            <div>Dataset is uploading</div>\n')
            # SOURCE LINE 144
        elif data_state == "queued":
            # SOURCE LINE 145
            __M_writer(u'            <div>')
            __M_writer(unicode(_('Job is waiting to run')))
            __M_writer(u'</div>\n            <div>\n                <a href="')
            # SOURCE LINE 147
            __M_writer(unicode(h.url_for( controller='dataset', action='show_params', dataset_id=dataset_id )))
            __M_writer(u'" target="galaxy_main" title=\'')
            __M_writer(unicode(_("View Details")))
            __M_writer(u'\' class="icon-button information tooltip"></a>\n')
            # SOURCE LINE 148
            if for_editing:
                # SOURCE LINE 149
                __M_writer(u'                    <a href="')
                __M_writer(unicode(h.url_for( controller='tool_runner', action='rerun', id=data.id )))
                __M_writer(u'" target="galaxy_main" title=\'')
                __M_writer(unicode(_("Run this job again")))
                __M_writer(u'\' class="icon-button arrow-circle tooltip"></a>\n')
                pass
            # SOURCE LINE 151
            __M_writer(u'            </div>\n')
            # SOURCE LINE 152
        elif data_state == "running":
            # SOURCE LINE 153
            __M_writer(u'            <div>')
            __M_writer(unicode(_('Job is currently running')))
            __M_writer(u'</div>\n            <div>\n                <a href="')
            # SOURCE LINE 155
            __M_writer(unicode(h.url_for( controller='dataset', action='show_params', dataset_id=dataset_id )))
            __M_writer(u'" target="galaxy_main" title=\'')
            __M_writer(unicode(_("View Details")))
            __M_writer(u'\' class="icon-button information tooltip"></a>\n')
            # SOURCE LINE 156
            if for_editing:
                # SOURCE LINE 157
                __M_writer(u'                    <a href="')
                __M_writer(unicode(h.url_for( controller='tool_runner', action='rerun', id=data.id )))
                __M_writer(u'" target="galaxy_main" title=\'')
                __M_writer(unicode(_("Run this job again")))
                __M_writer(u'\' class="icon-button arrow-circle tooltip"></a>\n')
                pass
            # SOURCE LINE 159
            __M_writer(u'            </div>\n')
            # SOURCE LINE 160
        elif data_state == "error":
            # SOURCE LINE 161
            if not data.purged:
                # SOURCE LINE 162
                __M_writer(u'                <div>')
                __M_writer(unicode(data.get_size( nice_size=True )))
                __M_writer(u'</div>\n')
                pass
            # SOURCE LINE 164
            __M_writer(u'            <div>\n                An error occurred running this job: <i>')
            # SOURCE LINE 165
            __M_writer(unicode(data.display_info().strip()))
            __M_writer(u'</i>\n            </div>\n            <div>\n')
            # SOURCE LINE 168
            if for_editing:
                # SOURCE LINE 169
                __M_writer(u'                    <a href="')
                __M_writer(unicode(h.url_for( controller='dataset', action='errors', id=data.id )))
                __M_writer(u'" target="galaxy_main" title="View or report this error" class="icon-button bug tooltip"></a>\n')
                pass
            # SOURCE LINE 171
            if data.has_data():
                # SOURCE LINE 172
                __M_writer(u'                    ')
                __M_writer(unicode(render_download_links( data, dataset_id )))
                __M_writer(u'\n')
                pass
            # SOURCE LINE 174
            __M_writer(u'                <a href="')
            __M_writer(unicode(h.url_for( controller='dataset', action='show_params', dataset_id=dataset_id )))
            __M_writer(u'" target="galaxy_main" title=\'')
            __M_writer(unicode(_("View Details")))
            __M_writer(u'\' class="icon-button information tooltip"></a>\n')
            # SOURCE LINE 175
            if for_editing:
                # SOURCE LINE 176
                __M_writer(u'                    <a href="')
                __M_writer(unicode(h.url_for( controller='tool_runner', action='rerun', id=data.id )))
                __M_writer(u'" target="galaxy_main" title=\'')
                __M_writer(unicode(_("Run this job again")))
                __M_writer(u'\' class="icon-button arrow-circle tooltip"></a>\n')
                pass
            # SOURCE LINE 178
            __M_writer(u'            </div>\n')
            # SOURCE LINE 179
        elif data_state == "discarded":
            # SOURCE LINE 180
            __M_writer(u'            <div>\n                The job creating this dataset was cancelled before completion.\n            </div>\n            <div>\n                <a href="')
            # SOURCE LINE 184
            __M_writer(unicode(h.url_for( controller='dataset', action='show_params', dataset_id=dataset_id )))
            __M_writer(u'" target="galaxy_main" title=\'')
            __M_writer(unicode(_("View Details")))
            __M_writer(u'\' class="icon-button information tooltip"></a>\n')
            # SOURCE LINE 185
            if for_editing:
                # SOURCE LINE 186
                __M_writer(u'                    <a href="')
                __M_writer(unicode(h.url_for( controller='tool_runner', action='rerun', id=data.id )))
                __M_writer(u'" target="galaxy_main" title=\'')
                __M_writer(unicode(_("Run this job again")))
                __M_writer(u'\' class="icon-button arrow-circle tooltip"></a>\n')
                pass
            # SOURCE LINE 188
            __M_writer(u'            </div>\n')
            # SOURCE LINE 189
        elif data_state == 'setting_metadata':
            # SOURCE LINE 190
            __M_writer(u'            <div>')
            __M_writer(unicode(_('Metadata is being Auto-Detected.')))
            __M_writer(u'</div>\n')
            # SOURCE LINE 191
        elif data_state == "empty":
            # SOURCE LINE 192
            __M_writer(u'            <div>')
            __M_writer(unicode(_('No data: ')))
            __M_writer(u'<i>')
            __M_writer(unicode(data.display_info()))
            __M_writer(u'</i></div>\n            <div>\n                <a href="')
            # SOURCE LINE 194
            __M_writer(unicode(h.url_for( controller='dataset', action='show_params', dataset_id=dataset_id )))
            __M_writer(u'" target="galaxy_main" title=\'')
            __M_writer(unicode(_("View Details")))
            __M_writer(u'\' class="icon-button information tooltip"></a>\n')
            # SOURCE LINE 195
            if for_editing:
                # SOURCE LINE 196
                __M_writer(u'                    <a href="')
                __M_writer(unicode(h.url_for( controller='tool_runner', action='rerun', id=data.id )))
                __M_writer(u'" target="galaxy_main" title=\'')
                __M_writer(unicode(_("Run this job again")))
                __M_writer(u'\' class="icon-button arrow-circle tooltip"></a>\n')
                pass
            # SOURCE LINE 198
            __M_writer(u'            </div>\n')
            # SOURCE LINE 199
        elif data_state in [ "ok", "failed_metadata" ]:
            # SOURCE LINE 200
            if data_state == "failed_metadata":
                # SOURCE LINE 201
                __M_writer(u'                <div class="warningmessagesmall" style="margin: 4px 0 4px 0">\n                    An error occurred setting the metadata for this dataset.\n')
                # SOURCE LINE 203
                if can_edit:
                    # SOURCE LINE 204
                    __M_writer(u'                        You may be able to <a href="')
                    __M_writer(unicode(h.url_for( controller='dataset', action='edit', dataset_id=dataset_id )))
                    __M_writer(u'" target="galaxy_main">set it manually or retry auto-detection</a>.\n')
                    pass
                # SOURCE LINE 206
                __M_writer(u'                </div>\n')
                pass
            # SOURCE LINE 208
            __M_writer(u'            <div>\n                ')
            # SOURCE LINE 209
            __M_writer(unicode(data.blurb))
            __M_writer(u'<br />\n                ')
            # SOURCE LINE 210
            __M_writer(unicode(_("format: ")))
            __M_writer(u' <span class="')
            __M_writer(unicode(data.ext))
            __M_writer(u'">')
            __M_writer(unicode(data.ext))
            __M_writer(u'</span>, \n                ')
            # SOURCE LINE 211
            __M_writer(unicode(_("database: ")))
            __M_writer(u'\n')
            # SOURCE LINE 212
            if data.dbkey == '?' and can_edit:
                # SOURCE LINE 213
                __M_writer(u'                    <a href="')
                __M_writer(unicode(h.url_for( controller='dataset', action='edit', dataset_id=dataset_id )))
                __M_writer(u'" target="galaxy_main">')
                __M_writer(unicode(_(data.dbkey)))
                __M_writer(u'</a>\n')
                # SOURCE LINE 214
            else:
                # SOURCE LINE 215
                __M_writer(u'                    <span class="')
                __M_writer(unicode(data.dbkey))
                __M_writer(u'">')
                __M_writer(unicode(_(data.dbkey)))
                __M_writer(u'</span>\n')
                pass
            # SOURCE LINE 217
            __M_writer(u'            </div>\n')
            # SOURCE LINE 218
            if data.display_info():
                # SOURCE LINE 219
                __M_writer(u'                <div class="info">')
                __M_writer(unicode(_('Info: ')))
                __M_writer(unicode(data.display_info()))
                __M_writer(u'</div>\n')
                pass
            # SOURCE LINE 221
            __M_writer(u'            <div>\n')
            # SOURCE LINE 222
            if data.has_data():
                # SOURCE LINE 223
                __M_writer(u'                    ')
                __M_writer(unicode(render_download_links( data, dataset_id )))
                __M_writer(u'\n                    \n                    <a href="')
                # SOURCE LINE 225
                __M_writer(unicode(h.url_for( controller='dataset', action='show_params', dataset_id=dataset_id )))
                __M_writer(u'" target="galaxy_main" title=\'')
                __M_writer(unicode(_("View Details")))
                __M_writer(u'\' class="icon-button information tooltip"></a>\n                    \n')
                # SOURCE LINE 227
                if for_editing:
                    # SOURCE LINE 228
                    __M_writer(u'                        <a href="')
                    __M_writer(unicode(h.url_for( controller='tool_runner', action='rerun', id=data.id )))
                    __M_writer(u'" target="galaxy_main" title=\'')
                    __M_writer(unicode(_("Run this job again")))
                    __M_writer(u'\' class="icon-button arrow-circle tooltip"></a>\n')
                    # SOURCE LINE 231
                    __M_writer(u'                        ')
 
                    visualizations = data.get_visualizations() 
                    ## HACK: if there are visualizations, only provide trackster for now
                    ##  since others are not ready. - comment out to see all WIP visualizations
                    if visualizations:
                        visualizations = [ vis for vis in visualizations if vis in [ 'trackster' ]  ]
                                            
                    
                    # SOURCE LINE 237
                    __M_writer(u'\n')
                    # SOURCE LINE 238
                    if visualizations:
                        # SOURCE LINE 239
                        __M_writer(u'                            <a href="')
                        __M_writer(unicode(h.url_for( controller='visualization' )))
                        __M_writer(u'" \n                               class="icon-button chart_curve tooltip visualize-icon"\n                               title="Visualize"\n                               dataset_id="')
                        # SOURCE LINE 242
                        __M_writer(unicode(dataset_id))
                        __M_writer(u'"\n')
                        # SOURCE LINE 243
                        if data.dbkey != '?':
                            # SOURCE LINE 244
                            __M_writer(u'                                   dbkey="')
                            __M_writer(unicode(data.dbkey))
                            __M_writer(u'" \n')
                            pass
                        # SOURCE LINE 246
                        __M_writer(u'                               visualizations="')
                        __M_writer(unicode(','.join(visualizations)))
                        __M_writer(u'"></a>\n')
                        pass
                    # SOURCE LINE 248
                    __M_writer(u'                        ')

                    isPhylogenyData = isinstance(data.datatype,  (Phyloxml, Nexus, Newick))
                                            
                    
                    # SOURCE LINE 250
                    __M_writer(u'\n')
                    # SOURCE LINE 251
                    if isPhylogenyData:
                        # SOURCE LINE 252
                        __M_writer(u'                                <a href="javascript:void(0)"  class="icon-button chart_curve phyloviz-add"\n                                   action-url="')
                        # SOURCE LINE 253
                        __M_writer(unicode(h.url_for( controller='phyloviz', action='-', dataset_id=dataset_id)))
                        __M_writer(u'"\n                                   new-url="')
                        # SOURCE LINE 254
                        __M_writer(unicode(h.url_for( controller='phyloviz', action='index', dataset_id=dataset_id)))
                        __M_writer(u'" title="View in Phyloviz"></a>\n')
                        pass
                    # SOURCE LINE 256
                    if trans.user:
                        # SOURCE LINE 257
                        if not display_structured:
                            # SOURCE LINE 258
                            __M_writer(u'                                <div style="float: right">\n                                    <a href="')
                            # SOURCE LINE 259
                            __M_writer(unicode(h.url_for( controller='tag', action='retag', item_class=data.__class__.__name__, item_id=dataset_id )))
                            __M_writer(u'" target="galaxy_main" title="Edit dataset tags" class="icon-button tags tooltip"></a>\n                                    <a href="')
                            # SOURCE LINE 260
                            __M_writer(unicode(h.url_for( controller='dataset', action='annotate', id=dataset_id )))
                            __M_writer(u'" target="galaxy_main" title="Edit dataset annotation" class="icon-button annotate tooltip"></a>\n                                </div>\n')
                            pass
                        # SOURCE LINE 263
                        __M_writer(u'                            <div style="clear: both"></div>\n                            <div class="tag-area" style="display: none">\n                                <strong>Tags:</strong>\n                                <div class="tag-elt"></div>\n                            </div>\n                            <div id="')
                        # SOURCE LINE 268
                        __M_writer(unicode(dataset_id))
                        __M_writer(u'-annotation-area" class="annotation-area" style="display: none">\n                                <strong>Annotation:</strong>\n                                <div id="')
                        # SOURCE LINE 270
                        __M_writer(unicode(dataset_id))
                        __M_writer(u'-annotation-elt" style="margin: 1px 0px 1px 0px" class="annotation-elt tooltip editable-text" title="Edit dataset annotation"></div>\n                            </div>\n                            \n')
                        pass
                    # SOURCE LINE 274
                else:
                    # SOURCE LINE 277
                    __M_writer(u'                        <div style="clear: both"></div>\n')
                    pass
                # SOURCE LINE 279
                __M_writer(u'                    <div style="clear: both"></div>\n')
                # SOURCE LINE 280
                for display_app in data.datatype.get_display_types():
                    # SOURCE LINE 281
                    __M_writer(u'                        ')
                    target_frame, display_links = data.datatype.get_display_links( data, display_app, app, request.base ) 
                    
                    __M_writer(u'\n')
                    # SOURCE LINE 282
                    if len( display_links ) > 0:
                        # SOURCE LINE 283
                        __M_writer(u'                            ')
                        __M_writer(unicode(data.datatype.get_display_label(display_app)))
                        __M_writer(u'\n')
                        # SOURCE LINE 284
                        for display_name, display_link in display_links:
                            # SOURCE LINE 285
                            __M_writer(u'                                <a target="')
                            __M_writer(unicode(target_frame))
                            __M_writer(u'" href="')
                            __M_writer(unicode(display_link))
                            __M_writer(u'">')
                            __M_writer(unicode(_(display_name)))
                            __M_writer(u'</a> \n')
                            pass
                        # SOURCE LINE 287
                        __M_writer(u'                            <br />\n')
                        pass
                    pass
                # SOURCE LINE 290
                for display_app in data.get_display_applications( trans ).itervalues():
                    # SOURCE LINE 291
                    __M_writer(u'                        ')
                    __M_writer(unicode(display_app.name))
                    __M_writer(u' \n')
                    # SOURCE LINE 292
                    for link_app in display_app.links.itervalues():
                        # SOURCE LINE 293
                        __M_writer(u'                            <a target="')
                        __M_writer(unicode(link_app.url.get( 'target_frame', '_blank' )))
                        __M_writer(u'" href="')
                        __M_writer(unicode(link_app.get_display_url( data, trans )))
                        __M_writer(u'">')
                        __M_writer(unicode(_(link_app.name)))
                        __M_writer(u'</a> \n')
                        pass
                    # SOURCE LINE 295
                    __M_writer(u'                        <br />\n')
                    pass
                # SOURCE LINE 297
            elif for_editing:
                # SOURCE LINE 298
                __M_writer(u'                    <a href="')
                __M_writer(unicode(h.url_for( controller='dataset', action='show_params', dataset_id=dataset_id )))
                __M_writer(u'" target="galaxy_main" title=\'')
                __M_writer(unicode(_("View Details")))
                __M_writer(u'\' class="icon-button information tooltip"></a>\n                    <a href="')
                # SOURCE LINE 299
                __M_writer(unicode(h.url_for( controller='tool_runner', action='rerun', id=data.id )))
                __M_writer(u'" target="galaxy_main" title=\'')
                __M_writer(unicode(_("Run this job again")))
                __M_writer(u'\' class="icon-button arrow-circle tooltip"></a>\n')
                pass
            # SOURCE LINE 301
            __M_writer(u'    \n                </div>\n')
            # SOURCE LINE 303
            if data.peek != "no peek":
                # SOURCE LINE 304
                __M_writer(u'                    <div><pre id="peek')
                __M_writer(unicode(data.id))
                __M_writer(u'" class="peek">')
                __M_writer(unicode(_(h.to_unicode(data.display_peek()))))
                __M_writer(u'</pre></div>\n')
                pass
            # SOURCE LINE 306
        else:
            # SOURCE LINE 307
            __M_writer(u'            <div>')
            __M_writer(unicode(_('Error: unknown dataset state "%s".') % data_state))
            __M_writer(u'</div>\n')
            pass
        # SOURCE LINE 309
        __M_writer(u'           \n')
        # SOURCE LINE 311
        __M_writer(u'                          \n')
        # SOURCE LINE 312
        if len( data.children ) > 0:
            # SOURCE LINE 315
            __M_writer(u'            ')

            children = []
            for child in data.children:
                if child.visible:
                    children.append( child )
            
            
            # SOURCE LINE 320
            __M_writer(u'\n')
            # SOURCE LINE 321
            if len( children ) > 0:
                # SOURCE LINE 322
                __M_writer(u'                <div>\n                    There are ')
                # SOURCE LINE 323
                __M_writer(unicode(len( children )))
                __M_writer(u' secondary datasets.\n')
                # SOURCE LINE 324
                for idx, child in enumerate(children):
                    # SOURCE LINE 325
                    __M_writer(u'                        ')
                    __M_writer(unicode(render_dataset( child, idx + 1, show_deleted_on_refresh = show_deleted_on_refresh )))
                    __M_writer(u'\n')
                    pass
                # SOURCE LINE 327
                __M_writer(u'                </div>\n')
                pass
            pass
        # SOURCE LINE 330
        __M_writer(u'\n    <div style="clear: both;"></div>\n\n    </div>\n        \n        \n    </div>\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


