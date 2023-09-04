$(document).ready(function() {
    let start_time = null;
    
    $("#typed-text").on("input", function() {
        if (start_time === null) {
            start_time = new Date().getTime() / 1000;
        }
        
        const typed_text = $(this).val();
        const typed_words = typed_text.trim().split(/\s+/);
        const num_words = typed_words.length;
        
        const end_time = new Date().getTime() / 1000;
        const time_elapsed = (end_time - start_time) / 60.0;  // in minutes
        
        const wpm = Math.floor(num_words / time_elapsed);
        $("#wpm-result").text("Your typing speed: " + wpm + " WPM");
    });
});
