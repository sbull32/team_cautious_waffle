function Data() {https://github.com/sbull32/team_cautious_waffle/blob/JTbranch/home2_df.csv
    jQuery.ajax({
        url: "https://github.com/sbull32/team_cautious_waffle/blob/JTbranch/home2_df.csv",
        type: 'get',
        dataType: 'text',
        success: function(data) {
            let lines = data.split('\n');
            let fields = lines[0].split(',');
            
            let output = [];
            
            for(let i = 1; i < lines.length; i++){
               let current = lines[i].split(',');
               let doc = {};
               for(let j = 0; j < fields.length; j++){
                   doc[fields[j]] = current[j];
               }
               output.push(doc);
            }       
            
            console.log(output);
        },
        error: function(jqXHR, textStatus, errorThrow){
            console.log(textStatus);
        }
    });
  }

// Attempting to find an intuitive way to utilize a JS query system to automatically pull data from one of the branches in our github to autopopulate the data on our html in a
// searchable/filterable dataset
