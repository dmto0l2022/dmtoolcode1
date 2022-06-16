      ActiveRecord::Schema.define(:version => 20091121174722) do

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

        create_table "sessions", :force => true do |t|
          t.string   "session_id", :default => "", :null => false
          t.text     "data"
          t.datetime "created_at"
          t.datetime "updated_at"
        end

        add_index "sessions", ["session_id"], :name => "index_sessions_on_session_id"
        add_index "sessions", ["updated_at"], :name => "index_sessions_on_updated_at"

        create_table "simple_captcha_data", :force => true do |t|
          t.string   "key",        :limit => 40
          t.string   "value",      :limit => 6
          t.datetime "created_at"
          t.datetime "updated_at"
        end

        create_table "users", :force => true do |t|
          t.string   "login"
          t.string   "email"
          t.string   "crypted_password",          :limit => 40
          t.string   "salt",                      :limit => 40
          t.datetime "created_at"
          t.datetime "updated_at"
          t.string   "remember_token"
          t.datetime "remember_token_expires_at"
          t.string   "reset_password_code"
          t.datetime "reset_password_code_until"
          t.string   "activation_code"
          t.datetime "activated_at"
        end

      end
