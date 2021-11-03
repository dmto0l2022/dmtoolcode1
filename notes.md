# Database Schema

  create_table "experiments", :force => true do |t|
    t.string "name"
  end

  create_table "limit_displays", :force => true do |t|
    t.integer  "limit_id"
    t.integer  "plot_id"
    t.string   "color",      :default => "k"
    t.string   "style",      :default => "line"
    t.datetime "created_at"
    t.datetime "updated_at"
  end

  create_table "limit_ownerships", :force => true do |t|
    t.integer  "user_id"
    t.integer  "limit_id"
    t.datetime "created_at"
    t.datetime "updated_at"
  end

  create_table "limits", :force => true do |t|
    t.string   "spin_dependency"
    t.string   "result_type",          :default => "Personal"
    t.string   "x_units",              :default => "GeV"
    t.string   "y_units",              :default => "cm^2"
    t.string   "x_rescale",            :default => "1"
    t.string   "y_rescale",            :default => "1"
    t.string   "default_color",        :default => "Blk"
    t.string   "default_style",        :default => "Line"
    t.text     "data_values"
    t.string   "data_label"
    t.string   "file_name"
    t.string   "data_comment"
    t.string   "data_reference"
    t.datetime "created_at"
    t.datetime "updated_at"
    t.integer  "creator_id"
    t.string   "experiment"
    t.integer  "rating",               :default => 0
    t.date     "date_of_announcement"
    t.boolean  "public",               :default => false
    t.boolean  "official",             :default => false
    t.date     "date_official"
    t.boolean  "greatest_hit",         :default => false
    t.date     "date_of_run_start"
    t.date     "date_of_run_end"
    t.integer  "year"
  end

  create_table "plot_ownerships", :force => true do |t|
    t.integer  "user_id"
    t.integer  "plot_id"
    t.datetime "created_at"
    t.datetime "updated_at"
  end

  create_table "plots", :force => true do |t|
    t.string   "name"
    t.string   "x_min",                          :default => "1"
    t.string   "x_max",                          :default => "10000"
    t.string   "y_min",                          :default => "-54"
    t.string   "y_max",                          :default => "-26"
    t.string   "x_units",                        :default => "GeV/c^2"
    t.string   "y_units",                        :default => "cm2"
    t.integer  "user_id"
    t.datetime "created_at"
    t.datetime "updated_at"
    t.binary   "plot_png",   :limit => 16777215
    t.binary   "legend_png", :limit => 16777215
    t.binary   "plot_eps",   :limit => 16777215
    t.binary   "legend_eps", :limit => 16777215
    t.boolean  "no_id",                          :default => false
  end

 
## Limit Interface

<p>
    <%= link_to 'New limit &raquo;', new_limit_path %>
</p>
<h2>Listing all limits</h2>

<% form_tag limits_path, :id => 'limits_search', :class => 'remote', :method => :get do %>

  <p class='fieldWrapper'>
  <% content_tag :label do %>
    Search for limits:
  <% end %>
  <%= text_field_tag("limits_search[text]", session[:limits_search][1]['text'], :autocomplete => 'off') %>
  <%= image_tag 'bar-spinner.gif', :alt => 'Searching...', :id => 'spinner', :style => 'margin-left:9px;display:none' %>
  </p>
  
  <table class='form'>
    <tr>
      <td><%= select_tag "limits_search[official][]",
                         options_for_select([["All Limits", "all"], ["Official Limits", "1"]],session[:limits_search][1]['official'] || 'all'),
                         {:size => 6} %></td>
      <td><%= select_tag "limits_search[result_type][]",
                         options_for_select([["All" , "all"], ["Experiment" , "Exp"], ["Projection", "Proj"], ["Theory" , "Th"], ["Other" , "Other"], ["Personal" , "Personal"]],session[:limits_search][1]['result_type'] || 'all'),
                         {:multiple => true, :size => 6} %></td>
        <!-- CAN COMMENT OUT THE BELOW LINE(S) IF IT DOESN'T WORK -->
<!--      <td><%= select_tag "limits_search[measurement_type][]",
                         options_for_select([["All" , "all"],  ["Direct" , "Dir"], ["Indirect" , "Ind"]],session[:limits_search][1]['measurement_type'] || 'all'),
                         {:multiple => true, :size => 6} %></td>
    -->    
        <td><%= select_tag "limits_search[spin_dependency][]",
                         options_for_select(Limit.spin_dependencies.sort,session[:limits_search][1]['spin_dependency'] || 'all'),
                         {:multiple => true, :size => 6} %></td>
      <td><%= select_tag "limits_search[experiment][]",
                         options_for_select(Limit.experiments.sort,session[:limits_search][1]['experiment'] || 'all'),
                         {:multiple => true, :size => 6} %></td>
      <td><%= select_tag "limits_search[year][]",
                         options_for_select([["All", "all"], ["2000", "2000"], ["2001", "2001"], ["2002", "2002"],["2003", "2003"], ["2004", "2004"], ["2005", "2005"],["2006", "2006"], ["2007", "2007"], ["2008", "2008"], ["2009", "2009"], ["2010", "2010"], ["2011", "2011"], ["2012", "2012"],["2013", "2013"],["2014", "2014"],["2014", "2014"],["2015", "2015"],["2016", "2016"],["2017", "2017"],["2018", "2018"],["2019", "2019"],["2020", "2020"]],session[:limits_search][1]['year'] || 'all'),
                         {:multiple => true, :size => 6} %></td>
      <td><%= select_tag "limits_search[greatest_hit][]",
                         options_for_select([["All", "all"], ["Greatest Hits", "1"]],session[:limits_search][1]['greatesthit'] || 'all'),
                         {:multiple => false, :size => 6} %></td>
    </tr>
  </table>

<% end %>
<% toggle_code = "$('spinner').toggle();" %>
<%= observe_form 'limits_search', :url => limits_path, :method => :get, :frequency => 1, :before => toggle_code, :complete => toggle_code %>

<div id='search_results'>
<%= render :partial => 'search_results' %>
</div>
