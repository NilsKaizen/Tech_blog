
// Checkbox Draft
draft = $('#draft')
// Button Create Post
b_c = $('#b_c')
// Alert Publish if Draft is not Selected
p_t = $('#publish')



draft.change(function () { alert_publish()})

function alert_publish() {
    if (draft.is(':checked')) {
        b_c.text('Save')
        b_c.css("background", "#3f8df2")
        p_t.text('')
    } else {
        p_t.text('Your post wil be published')
        b_c.css("background", "#3ff278")
        b_c.css("color", "black")
        b_c.text('Publish') 
    }
}