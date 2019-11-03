function makeMap() {
    var mapMinZoom = -1
    var mapMaxZoom = 3;

    var map = L.map('map', {
        minZoom: mapMinZoom,
        maxZoom: mapMaxZoom,
        crs: L.CRS.Simple
    })

    var bounds = [[-322,-556], [397,533]];
    var image = L.imageOverlay('static/Helmaria-fixed.jpg', bounds).addTo(map);
    map.fitBounds(bounds);

    var center = L.latLng([ 0, 0 ]);
    addMarker(center, map, false, "Helmaria")
    map.setView(center, 0.5)

    // USing Leaflet.Coordinates plugin at https://github.com/MrMufflon/Leaflet.Coordinates

    // Patch first to avoid longitude wrapping.
    L.Control.Coordinates.include({
        _update: function(evt) {
          var pos = evt.latlng,
            opts = this.options;
          if (pos) {
            //pos = pos.wrap(); // Remove that instruction.
            this._currentPos = pos;
            this._inputY.value = L.NumberFormatter.round(pos.lat, opts.decimals, opts.decimalSeperator);
            this._inputX.value = L.NumberFormatter.round(pos.lng, opts.decimals, opts.decimalSeperator);
            this._label.innerHTML = this._createCoordinateLabel(pos);
          }
        }
    });

    L.control.coordinates({
        position: "bottomleft",
        decimals: 0, //optional default 4
        decimalSeperator: ".", //optional default "."
        labelTemplateLat: "Latitude: {y}", //optional default "Lat: {y}"
        labelTemplateLng: "Longitude: {x}", //optional default "Lng: {x}"
        enableUserInput: true, //optional default true
        useDMS: false, //optional default false
        useLatLngOrder: true, //ordering of labels, default false-> lng-lat
        markerType: L.marker, //optional default L.marker
        markerProps: {} //optional default {}
    }).addTo(map);

    return map;
}

function onPopupOpen() {
    var tempMarker = this;

    $("#myModal").on('show.bs.modal', function(e) {
        $("#latitude").val(tempMarker.getLatLng().lat);
        $("#longitude").val(tempMarker.getLatLng().lng);
    });

    $("#myModal").on('hide.bs.modal', function(e) {
        $("#location_name").val('');
        $("#wiki_link").val('');
        $("#latitude").val('');
        $("#longitude").val('');
    });

    // To remove marker on click of delete button in the popup of marker
    $(".marker-delete-button").click(function () {
        map.removeLayer(tempMarker);
    });
}

function addMarker(latlng, map, popup, title) {
    var lat = latlng.lat;
    var lng = latlng.lng;

    // Add marker to map at click location; add popup window
    var newMarker = new L.marker(latlng).addTo(map);
    newMarker.bindPopup('<h4>' + title + '</h4><br><button type="button" class="btn btn-info" data-toggle="modal" data-target="#myModal">Add details</button> <button type="button" class="btn btn-danger marker-delete-button">Remove</button>');

    newMarker.on('popupopen', onPopupOpen);
    if (popup) {
        newMarker.openPopup();
    }
}

var map = makeMap();

map.on('click', function(e){
        addMarker(e.latlng, map, true, "New marker");
});