define(["libs/backbone/backbone-relational"], function() {
/**
 * A dataset. In Galaxy, datasets are associated with a history, so
 * this object is also known as a HistoryDatasetAssociation.
 */
var Dataset = Backbone.RelationalModel.extend({
    defaults: {
        id: '',
        type: '',
        name: '',
        hda_ldda: 'hda'
    },

    urlRoot: galaxy_paths.get('datasets_url')
});

var DatasetCollection = Backbone.Collection.extend({
    model: Dataset
});

return {
	Dataset: Dataset,
	DatasetCollection: DatasetCollection
};

});
