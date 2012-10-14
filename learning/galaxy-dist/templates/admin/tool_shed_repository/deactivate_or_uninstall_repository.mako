<%inherit file="/base.mako"/>
<%namespace file="/message.mako" import="render_msg" />
<%namespace file="/admin/tool_shed_repository/common.mako" import="*" />

<br/><br/>
<ul class="manage-table-actions">
    <li><a class="action-button" id="repository-${repository.id}-popup" class="menubutton">Repository Actions</a></li>
    <div popupmenu="repository-${repository.id}-popup">
        <a class="action-button" href="${h.url_for( controller='admin_toolshed', action='manage_repository', id=trans.security.encode_id( repository.id ) )}">Manage repository</a>
        %if repository.has_readme:
            <a class="action-button" href="${h.url_for( controller='admin_toolshed', action='view_readme', id=trans.security.encode_id( repository.id ) )}">View README</a>
        %endif
        <a class="action-button" href="${h.url_for( controller='admin_toolshed', action='browse_repository', id=trans.security.encode_id( repository.id ) )}">Browse repository files</a>
        <a class="action-button" href="${h.url_for( controller='admin_toolshed', action='check_for_updates', id=trans.security.encode_id( repository.id ) )}">Get repository updates</a>
        %if repository.can_reset_metadata:
            <a class="action-button" href="${h.url_for( controller='admin_toolshed', action='reset_repository_metadata', id=trans.security.encode_id( repository.id ) )}">Reset repository metadata</a>
        %endif
        %if repository.tool_dependencies:
            <% tool_dependency_ids = [ trans.security.encode_id( td.id ) for td in repository.tool_dependencies ] %>
            <a class="action-button" href="${h.url_for( controller='admin_toolshed', action='manage_tool_dependencies', tool_dependency_ids=tool_dependency_ids )}">Manage tool dependencies</a>
        %endif
    </div>
</ul>

%if message:
    ${render_msg( message, status )}
%endif

<div class="toolForm">
    <div class="toolFormTitle">${repository.name}</div>
    <div class="toolFormBody">
        <form name="deactivate_or_uninstall_repository" id="deactivate_or_uninstall_repository" action="${h.url_for( controller='admin_toolshed', action='deactivate_or_uninstall_repository', id=trans.security.encode_id( repository.id ) )}" method="post" >
            <div class="form-row">
                <label>Description:</label>
                ${repository.description}
                <div style="clear: both"></div>
            </div>
            <div class="form-row">
                <label>Revision:</label>
                ${repository.changeset_revision}</a>
            </div>
            <div class="form-row">
                <label>Tool shed:</label>
                ${repository.tool_shed}
                <div style="clear: both"></div>
            </div>
            <div class="form-row">
                <label>Owner:</label>
                ${repository.owner}
            </div>
            <div class="form-row">
                <label>Deleted:</label>
                ${repository.deleted}
            </div>
            <div class="form-row">
                ${remove_from_disk_check_box.get_html()}
                <label for="repository" style="display: inline;font-weight:normal;">Check to uninstall or leave blank to deactivate</label>
                <br/><br/>
                <label>Deactivating this repository will result in the following:</label>
                <div class="toolParamHelp" style="clear: both;">
                    * The repository and all of it's contents will remain on disk.
                </div>
                %if repository.includes_tools:
                    <div class="toolParamHelp" style="clear: both;">
                        * The repository's tools will not be loaded into the tool panel.
                    </div>
                %endif
                %if repository.includes_tool_dependencies:
                    <div class="toolParamHelp" style="clear: both;">
                        * The repository's installed tool dependencies will remain on disk.
                    </div>
                %endif
                %if repository.includes_datatypes:
                    <div class="toolParamHelp" style="clear: both;">
                        * The repository's datatypes, datatype converters and display applications will be eliminated from the datatypes registry.
                    </div>
                %endif
                <div class="toolParamHelp" style="clear: both;">
                    * The repository record's deleted column in the tool_shed_repository database table will be set to True.
                </div>
                <br/>
                <label>Uninstalling this repository will result in the following:</label>
                <div class="toolParamHelp" style="clear: both;">
                    * The repository and all of it's contents will be removed from disk.
                </div>
                %if repository.includes_tools:
                    <div class="toolParamHelp" style="clear: both;">
                        * The repository's tool tag sets will be removed from the tool config file in which they are defined.
                    </div>
                %endif
                %if repository.includes_tool_dependencies:
                    <div class="toolParamHelp" style="clear: both;">
                        * The repository's installed tool dependencies will be removed from disk.
                    </div>
                    <div class="toolParamHelp" style="clear: both;">
                        * Each associated tool dependency record's status column in the tool_dependency database table will be set to 'Uninstalled'.
                    </div>
                %endif
                %if repository.includes_datatypes:
                    <div class="toolParamHelp" style="clear: both;">
                        * The repository's datatypes, datatype converters and display applications will be eliminated from the datatypes registry.
                    </div>
                %endif
                <div class="toolParamHelp" style="clear: both;">
                    * The repository record's deleted column in the tool_shed_repository database table will be set to True.
                </div>
                <div class="toolParamHelp" style="clear: both;">
                    * The repository record's uninstalled column in the tool_shed_repository database table will be set to True.
                </div>
                <div style="clear: both"></div>
            </div>
            <div class="form-row">
                <input type="submit" name="deactivate_or_uninstall_repository_button" value="Deactivate or Uninstall"/>
            </div>
        </form>
    </div>
</div>
