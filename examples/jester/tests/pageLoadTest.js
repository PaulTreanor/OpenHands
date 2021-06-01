/*
    Contains tests to see if major elements of the 3 tabs in the app are loading correctly. 
*/

module.exports = {
    // Camera page loads when app URL is loaded
    'Camera tab load test': function(browser) {
        browser
            .url('http://localhost:8080/')
            .waitForElementVisible('.brand')
            .assert.containsText(".brand", "Jester")
            .assert.containsText("#photo", "Photo");   

    },

    'Camera preview load test': function(browser) {
        browser
            .url('http://localhost:8080/')
            .waitForElementVisible('#preview')
            .assert.elementPresent("#preview");
    },

    // Gallery page loads when gallery button is clicked 
    'Gallery page load test': function(browser) {
        browser
        .url('http://localhost:8080/')
        .waitForElementVisible("#galleryButton")
        .click("#galleryButton", function(){
            browser
                .waitForElementVisible('#photoTitle')
                .assert.elementPresent('#photoTitle');                 
        })
    },

    // Info page loads when info button is clicked
    'Info page load test': function(browser) {
        browser
        .url('http://localhost:8080/')
        .waitForElementVisible("#infoButton")
        .click("#infoButton", function(){
            browser
                .waitForElementVisible('.alert')
                .assert.elementPresent('.alert');              
        })
    }
}