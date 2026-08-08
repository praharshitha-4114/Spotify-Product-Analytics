INSERT INTO subscriptions
(plan_name, monthly_price, max_devices, audio_quality, offline_download, ad_free)
VALUES
('Free', 0.00, 1, 'Standard', FALSE, FALSE),
('Individual', 9.99, 1, 'Very High', TRUE, TRUE),
('Duo', 14.99, 2, 'Very High', TRUE, TRUE),
('Family', 16.99, 6, 'Very High', TRUE, TRUE),
('Student', 5.99, 1, 'Very High', TRUE, TRUE);

select * FROM subscriptions;