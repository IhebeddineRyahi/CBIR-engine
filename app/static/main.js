
$("#searching").hide();
      $("#results-table").hide();
      $("#error").hide()
      var data = [];
      $(function() {
        console.log( "ready!" );
        $(".img").click(function() {
          $("#results").empty();
          $("#results-table").hide();
          $("#error").hide();
          $(".img").removeClass("active")
          $(this).addClass("active")
          var image = $(this).attr("src")
          console.log(image)
          $("#searching").show();
          console.log("searching...")
          $.ajax({
            type: "POST",
            url: "/search",
            data : { img : image },
            success: function(result) {
              console.log(result.results);
              var data = result.results;
              $("#results-table").show();
              for (i = 0; i < data.length; i++) {
                $("#results").append('<tr><th><a><img src="data:image/png;base64,'+ data[i]["URL"]+'" alt="'+data[i]["image"]+'" class="result-img"></a></th><th>'+data[i]['score']+'</th></tr>')
              };
              $("#searching").hide();
            },
            error: function(error) {
              console.log(error);
              $("#error").append()
            }
          });
        });
      });