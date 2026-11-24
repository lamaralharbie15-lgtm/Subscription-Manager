import storage
import logic
import ui

def main():
    # 1. تحميل الاشتراكات المحفوظة سابقاً عند تشغيل البرنامج
    subscriptions = storage.load_subscriptions()
    
    while True:
        # 2. عرض القائمة الرئيسية وأخذ اختيار المستخدم من ملف ui
        choice = ui.show_menu()
        
        if choice == "1":
            # إضافة اشتراك جديد
            new_sub = ui.get_new_subscription()
            subscriptions.append(new_sub)
            storage.save_subscriptions(subscriptions)
            ui.show_message("✅ Subscription saved successfully!")
            
        elif choice == "2":
            # عرض جميع الاشتراكات الحالية
            ui.display_subscriptions(subscriptions)
            
        elif choice == "3":
            # حساب وعرض إجمالي التكاليف الشهرية والسنوية من ملف logic
            monthly_total, yearly_total = logic.calculate_totals(subscriptions)
            ui.display_totals(monthly_total, yearly_total)
            
        elif choice == "4":
            # فحص الاشتراكات التي اقترب موعد تجديدها من ملف logic
            upcoming = logic.get_upcoming_renewals(subscriptions)
            ui.display_upcoming(upcoming)
            
        elif choice == "5":
            # حذف اشتراك
            index = ui.get_delete_index(subscriptions)
            if index is not None and 0 <= index < len(subscriptions):
                removed = subscriptions.pop(index)
                storage.save_subscriptions(subscriptions)
                ui.show_message(f"🗑️ Deleted subscription: {removed['name']}")
                
        elif choice == "0":
            # الخروج من البرنامج
            ui.show_message("👋 Thank you for using Subscription Manager!")
            break
        else:
            ui.show_message("⚠️ Invalid option, please try again.")

if __name__ == "__main__":
    main()