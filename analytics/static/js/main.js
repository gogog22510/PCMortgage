// Get token
function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
var csrftoken = getCookie('csrftoken');

var table1Element = document.querySelector('#t1');
var config = {
	data: dataObject,
	licenseKey: 'non-commercial-and-evaluation',
	stretchH: 'all',
	width: 400,
	height: 500,
	autoWrapRow: true,
	rowHeaders: true
};

// initialize hook
var cellupdate = function(changes, source) {
	if(changes != null) {
		var evt = changes[0];
		var changeEvt = {
			row: evt[0],
			col: evt[1],
			pre: evt[2],
			val: evt[3]
		};
		// console.log(changeEvt);
		$.ajax({
			url: '/table/t1',
			type: 'PUT',
			headers: {'X-CSRFToken': csrftoken},
			data: changeEvt,
			dataType : 'json',
			success: function(result) {
				// Do something with the result
				console.log(result);
			}
		});
	}
};

config['afterChange'] = function(changes, source) {
	cellupdate(changes, source);
};

// initialize table
var t1 = new Handsontable(table1Element, config);
t1.updateSettings({
	cells: function (row, col) {
		var cellProperties = {};

		if (editState[row][col] == 0) {
			cellProperties.readOnly = true;
		}

		return cellProperties;
	}
});
