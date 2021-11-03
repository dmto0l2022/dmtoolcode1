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

 
