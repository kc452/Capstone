<%inherit file="/webapps/galaxy/base_panels.mako"/>

<%def name="init()">
<%
    self.has_left_panel=False
    self.has_right_panel=False
    self.active_view="shared"
    self.message_box_visible=False
%>
</%def>

<%def name="stylesheets()">
    ${parent.stylesheets()}
    ${h.css( "autocomplete_tagging" )}
    <style type="text/css">
    #new_history_p{
        line-height:2.5em;
        margin:0em 0em .5em 0em;
    }
    #new_history_cbx{
        margin-right:.5em;
    }
    #new_history_input{
        display:none;
        line-height:1em;
    }
    #ec_button_container{
        float:right;
    }
    #hidden_options{
        display:none;
    }
    div.toolForm{
        margin-top: 10px;
        margin-bottom: 10px;
    }
    div.toolFormTitle{
        cursor:pointer;
    }
    .title_ul_text{
        text-decoration:underline;
    }
    .step-annotation {
        margin-top: 0.25em;
        font-weight: normal;
        font-size: 97%;
    }
    .workflow-annotation {
        margin-bottom: 1em;
    }
    #loading_indicator{
            position:fixed;
            top:40px;
    }
    </style>
</%def>

<%def name="javascripts()">
    ${parent.javascripts()}
    <script type="text/javascript">
        var ACCOUNT_URL = "${h.url_for( controller='/cloudlaunch', action='get_account_info')}";
        var PKEY_DL_URL = "${h.url_for( controller='/cloudlaunch', action='get_pkey')}";
        $(document).ready(function(){
            $('#id_existing_instance').change(function(){
                var ei_name = $(this).val();
                if (ei_name === "New Cluster"){
                    //For new instances, need to see the cluster name field.
                    $('#id_cluster_name').val("New Cluster")
                    $('#cluster_name_wrapper').show('fast');
                }else{
                    //Hide the Cluster Name field, but set the value
                    $('#id_cluster_name').val($(this).val());
                    $('#cluster_name_wrapper').hide('fast');
                }
            });
             //When id_secret and id_key are complete, submit to get_account_info
            $("#id_secret, #id_key_id").bind("change paste keyup", function(){
                secret_el = $("#id_secret");
                key_el = $("#id_key_id");
                if (secret_el.val().length === 40 && key_el.val().length === 20){
                    //Submit these to get_account_info, unhide fields, and update as appropriate
                    $.getJSON(ACCOUNT_URL,
                                {key_id: key_el.val(),secret:secret_el.val()},
                                function(result){
                                    var kplist = $("#id_keypair");
                                    var clusterlist = $("#id_existing_instance");
                                    kplist.find('option').remove();
                                    clusterlist.find('option').remove();
                                    //Update fields with appropriate elements
                                    if (_.size(result.clusters) > 0){
                                        clusterlist.append($('<option/>').val('New Cluster').text('New Cluster'));
                                        _.each(result.clusters, function(cluster, index){
                                            clusterlist.append($('<option/>').val(cluster.name).text(cluster.name));
                                        });
                                        $('#existing_instance_wrapper').show();
                                    }
                                    if (!_.include(result.keypairs, '${default_keypair}')){
                                        kplist.append($('<option/>').val('${default_keypair}').text('Create New - ${default_keypair}'));
                                    }
                                    _.each(result.keypairs, function(keypair, index){
                                        kplist.append($('<option/>').val(keypair).text(keypair));
                                    });
                                    $('#hidden_options').show('fast');
                                });
                }
            });
            $('#loading_indicator').ajaxStart(function(){
                $(this).show('fast');
            }).ajaxStop(function(){
                $(this).hide('fast');
            });
            $('form').ajaxForm({
                    type: 'POST',
                    dataType: 'json',
                    beforeSubmit: function(data){
                        //Hide the form, show pending box with spinner.
                        $('#launchFormContainer').hide('fast');
                        $('#responsePanel').show('fast');
                    },
                    success: function(data){
                        //Success Message, link to key download if required, link to server itself.
                        $('#launchPending').hide('fast');
                        //Check for success/error.
                        if (data.error){
                            //Apologize profusely.
                            $("launchPending").hide();
                            $("#launchError").show();
                        }else{
                            //Set appropriate fields (dns, key, ami) and then display.
                            if(data.kp_material_tag){
                                var kp_download_link = $('<a/>').attr('href', PKEY_DL_URL + '?kp_material_tag=' + data.kp_material_tag)
                                                                .attr('target','_blank')
                                                                .text("Download your key now");
                                $('#keypairInfo').append(kp_download_link);
                                $('#keypairInfo').show();
                            }
                            $('.kp_name').text(data.kp_name);
                            $('#instance_id').text(data.instance_id);
                            $('#image_id').text(data.image_id);
                            $('#instance_link').html($('<a/>')
                                .attr('href', 'http://' + data.public_dns_name + '/cloud')
                                .attr('target','_blank')
                                .text(data.public_dns_name + '/cloud'));
                            $('#instance_dns').text(data.public_dns_name);
                            $('#launchSuccess').show('fast');
                        }
                    }
            });
        });
    </script>
</%def>

<%def name="center_panel()">
    <div style="overflow: auto; height: 100%;">
        <div class="page-container" style="padding: 10px;">
        <div id="loading_indicator"></div>
            <h2>Launch a Galaxy Cloud Instance</h2>
              <div id="launchFormContainer" class="toolForm">
                    <form id="cloudlaunch_form" action="${h.url_for( controller='/cloudlaunch', action='launch_instance')}" method="post">

                    <p>To launch a Galaxy Cloud Cluster, enter your AWS Secret Key ID, and Secret Key.  Galaxy will use
                    these to present appropriate options for launching your cluster.   Note that using this form to
                    launch computational resources in the Amazon Cloud will result in   costs to the account indicated
                    above.  See <a href="http://aws.amazon.com/ec2/pricing/">Amazon's pricing</a> for more information.
                    options for launching your cluster.</p> </p>

                    <div class="form-row">
                        <label for="id_key_id">Key ID</label>
                        <input type="text" size="30" maxlength="20" name="key_id" id="id_key_id" value=""/><br/>
                        <div class="toolParamHelp">
                            This is the text string that uniquely identifies your account, found in the 
                            <a href="https://portal.aws.amazon.com/gp/aws/securityCredentials">Security Credentials section of the AWS Console</a>.
                        </div>
                    </div>

                    <div class="form-row">
                        <label for="id_secret">Secret Key</label>
                        <input type="text" size="50" maxlength="40" name="secret" id="id_secret" value=""/><br/>
                        <div class="toolParamHelp">
                            This is your AWS Secret Key, also found in the <a href="https://portal.aws.amazon.com/gp/aws/securityCredentials">Security
Credentials section of the AWS Console</a>.  </div>
                    </div>

                    <div id="hidden_options">
                        <div id='existing_instance_wrapper' style="display:none;" class="form-row">
                                <label for="id_existing_instance">Instances in your account</label>
                                <select name="existing_instance" id="id_existing_instance">
                                </select>
                        </div>
                        <div id='cluster_name_wrapper' class="form-row">
                            <label for="id_cluster_name">Cluster Name</label>
                            <input type="text" size="40" class="text-and-autocomplete-select" name="cluster_name" id="id_cluster_name"/><br/>
                            <div class="toolParamHelp">
                                This is the name for your cluster.  You'll use this when you want to restart.
                            </div>
                        </div>

                        <div class="form-row">
                            <label for="id_password">Cluster Password</label>
                            <input type="password" size="40" name="password" id="id_password"/><br/>
                        </div>

                        <div class="form-row">
                            <label for="id_keypair">Key Pair</label>
                            <select name="keypair" id="id_keypair">
                                <option name="Create" value="cloudman_keypair">cloudman_keypair</option>
                            </select>
                        </div>

                        %if share_string:
                            <input type='hidden' name='share_string' value='${share_string}'/>
                        %else:
                        <!-- DBEDIT temporary hide share string due to it being broken on the cloudman end -->
                        <div class="form-row" style="display:none;">
                            <label for="id_share_string">Instance Share String (optional)</label>
                            <input type="text" size="120" name="share_string" id="id_share_string"/><br/>
                        </div>
                        %endif

                        <div class="form-row">
                            <label for="id_instance_type">Instance Type</label>
                            <select name="instance_type" id="id_instance_type">
                                <option value="m1.large">Large</option>
                                <option value="m1.xlarge">Extra Large</option>
                                <option value="m2.4xlarge">High-Memory Quadruple Extra Large</option>
                            </select>
                        </div>
                        <div class="form-row">
                            <p>Requesting the instance may take a moment, please be patient.  Do not refresh your browser or navigate away from the page</p>
                            <input type="submit" value="Submit" id="id_submit"/>
                        </div>
                    </div>
                        <div class="form-row">
                        <div id="loading_indicator" style="position:relative;left:10px;right:0px"></div>
                        </div>
                    </form>
                </div>
                <div id="responsePanel" class="toolForm" style="display:none;">
                        <div id="launchPending">Launch Pending, please be patient.</div>
                        <div id="launchError" style="display:none;">ERROR</div>
                        <div id="launchSuccess" style="display:none;">
                            <div id="keypairInfo" style="display:none;margin-bottom:20px;">
                                <h3>Very Important Key Pair Information</h3>
                                <p>A new key pair named <strong><span class="kp_name">kp_name</span></strong> has been created in your AWS
                                account and will be used to access this instance via ssh. It is
                                <strong>very important</strong> that you save the following private key
                                as it is not saved on this Galaxy instance and will be permanently lost if not saved.  Additionally, this link will
                                only allow a single download, after which the key is removed from the Galaxy server permanently.<br/>
                            </div>
                            <div>
                                <h3>Access Information</h3>
                                <ul>
                                    <li>Your instance '<span id="instance_id">undefined</span>' has been successfully launched using the
                                '<span id="image_id">undefined</span>' AMI.</li>
                                <li>While it may take a few moments to boot, you will be able to access the cloud control
                                panel at <span id="instance_link">undefined.</span>.</li>
                            <li>SSH access is also available using your private key.  From the terminal, you would execute something like:</br>&nbsp;&nbsp;&nbsp;&nbsp;`ssh -i <span class="kp_name">undefined</span>.pem ubuntu@<span
id="instance_dns">undefined</span>`</li>
                                </ul>
                        </div>
                </div>
        </div>
    </div>
</%def>
