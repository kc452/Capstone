<%inherit file="/base.mako"/>
<%namespace file="/message.mako" import="render_msg" />
<%namespace file="/webapps/community/common/common.mako" import="*" />
<%namespace file="/webapps/community/repository/common.mako" import="*" />

<%
    from galaxy.web.framework.helpers import time_ago
    from galaxy.tool_shed.encoding_util import tool_shed_encode

    in_tool_shed = trans.webapp.name == 'community'
    is_admin = trans.user_is_admin()
    is_new = repository.is_new
    can_manage = is_admin or trans.user == repository.user
    can_contact_owner = in_tool_shed and trans.user and trans.user != repository.user
    can_push = in_tool_shed and trans.app.security_agent.can_push( trans.user, repository )
    can_upload = can_push
    can_download = in_tool_shed and not is_new and ( not is_malicious or can_push )
    can_browse_contents = in_tool_shed and not is_new
    can_rate = in_tool_shed and not is_new and trans.user and repository.user != trans.user
    can_view_change_log = in_tool_shed and not is_new
    if can_push:
        browse_label = 'Browse or delete repository tip files'
    else:
        browse_label = 'Browse repository tip files'
    has_readme = metadata and 'readme' in metadata
%>

<%!
   def inherit(context):
       if context.get('use_panels'):
           return '/webapps/community/base_panels.mako'
       else:
           return '/base.mako'
%>
<%inherit file="${inherit(context)}"/>

<%def name="render_workflow( repository_metadata_id, workflow_name )">
    <% center_url = h.url_for( controller='workflow', action='generate_workflow_image', repository_metadata_id=repository_metadata_id, workflow_name=tool_shed_encode( workflow_name ) ) %>
    <iframe name="galaxy_main" id="galaxy_main" frameborder="0" style="position: absolute; width: 100%; height: 100%;" src="${center_url}"> </iframe>
</%def>

<br/><br/>
<ul class="manage-table-actions">
    %if in_tool_shed:
        %if is_new and can_upload:
            <a class="action-button" href="${h.url_for( controller='upload', action='upload', repository_id=trans.security.encode_id( repository.id ) )}">Upload files to repository</a>
        %else:
            <li><a class="action-button" id="repository-${repository.id}-popup" class="menubutton">Repository Actions</a></li>
            <div popupmenu="repository-${repository.id}-popup">
                %if can_upload:
                    <a class="action-button" href="${h.url_for( controller='upload', action='upload', repository_id=trans.security.encode_id( repository.id ) )}">Upload files to repository</a>
                %endif
                %if can_manage:
                    <a class="action-button" href="${h.url_for( controller='repository', action='manage_repository', id=trans.app.security.encode_id( repository.id ), changeset_revision=repository.tip )}">Manage repository</a>
                %else:
                    <a class="action-button" href="${h.url_for( controller='repository', action='view_repository', id=trans.app.security.encode_id( repository.id ), changeset_revision=repository.tip )}">View repository</a>
                %endif
                %if has_readme:
                    <a class="action-button" href="${h.url_for( controller='repository', action='view_readme', id=trans.app.security.encode_id( repository.id ), changeset_revision=changeset_revision )}">View README</a>
                %endif
                %if can_view_change_log:
                    <a class="action-button" href="${h.url_for( controller='repository', action='view_changelog', id=trans.app.security.encode_id( repository.id ) )}">View change log</a>
                %endif
                %if can_rate:
                    <a class="action-button" href="${h.url_for( controller='repository', action='rate_repository', id=trans.app.security.encode_id( repository.id ) )}">Rate repository</a>
                %endif
                %if can_browse_contents:
                    <a class="action-button" href="${h.url_for( controller='repository', action='browse_repository', id=trans.app.security.encode_id( repository.id ) )}">${browse_label}</a>
                %endif
                %if can_contact_owner:
                    <a class="action-button" href="${h.url_for( controller='repository', action='contact_owner', id=trans.security.encode_id( repository.id ) )}">Contact repository owner</a>
                %endif
                %if can_download:
                    <a class="action-button" href="${h.url_for( controller='repository', action='download', repository_id=trans.app.security.encode_id( repository.id ), changeset_revision=changeset_revision, file_type='gz' )}">Download as a .tar.gz file</a>
                    <a class="action-button" href="${h.url_for( controller='repository', action='download', repository_id=trans.app.security.encode_id( repository.id ), changeset_revision=changeset_revision, file_type='bz2' )}">Download as a .tar.bz2 file</a>
                    <a class="action-button" href="${h.url_for( controller='repository', action='download', repository_id=trans.app.security.encode_id( repository.id ), changeset_revision=changeset_revision, file_type='zip' )}">Download as a zip file</a>
                %endif
            </div>
        %endif
    %else:
        <li><a class="action-button" id="repository-${repository.id}-popup" class="menubutton">Repository Actions</a></li>
        <div popupmenu="repository-${repository.id}-popup">
            <li><a class="action-button" href="${h.url_for( controller='workflow', action='import_workflow', repository_metadata_id=repository_metadata_id, workflow_name=tool_shed_encode( workflow_name ) )}">Import workflow to local Galaxy</a></li>
            <li><a class="action-button" href="${h.url_for( controller='repository', action='install_repositories_by_revision', repository_ids=trans.security.encode_id( repository.id ), changeset_revisions=changeset_revision )}">Install repository to local Galaxy</a></li>
        </div>
        <li><a class="action-button" id="toolshed-${repository.id}-popup" class="menubutton">Tool Shed Actions</a></li>
        <div popupmenu="toolshed-${repository.id}-popup">
            <a class="action-button" href="${h.url_for( controller='repository', action='browse_valid_categories' )}">Browse valid repositories</a>
            <a class="action-button" href="${h.url_for( controller='repository', action='find_tools' )}">Search for valid tools</a>
            <a class="action-button" href="${h.url_for( controller='repository', action='find_workflows' )}">Search for workflows</a>
        </div>
    %endif
</ul>

%if message:
    ${render_msg( message, status )}
%endif

<div class="toolFormTitle">${workflow_name}</div>
<div class="form-row">
    <b>Boxes are red when tools are not available in this repository</b>
    <div class="toolParamHelp" style="clear: both;">
        (this page displays SVG graphics)
    </div>
</div>
<br clear="left"/>

${render_workflow( repository_metadata_id, workflow_name )}
