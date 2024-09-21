import pandas as pd
from sklearn.linear_model import LassoLars
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.compose import ColumnTransformer
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score, explained_variance_score
import warnings

warnings.filterwarnings("ignore", category=UserWarning, module='sklearn.linear_model._least_angle')

data = pd.read_csv(r'C:\Users\anuli\OneDrive\Desktop\Fossil Age Estimation\Datasets\fossil_data.csv')

X = data.drop(['Age'], axis=1)
y = data['Age']

categorical_cols = X.select_dtypes(include='object').columns
numerical_cols = X.select_dtypes(include=['int64', 'float64']).columns

ct = ColumnTransformer([
    ('onehot', OneHotEncoder(handle_unknown='ignore'), categorical_cols),
    ('scaler', StandardScaler(), numerical_cols)
], remainder='passthrough')

X = ct.fit_transform(X)

if hasattr(X, "toarray"):
    X = X.toarray()

X_train, X_temp, y_train, y_temp = train_test_split(X, y, test_size=0.3, random_state=42)
X_val, X_test, y_val, y_test = train_test_split(X_temp, y_temp, test_size=0.5, random_state=42)

model = LassoLars(alpha=0.1)  
model.fit(X_train, y_train)

for name, dataset, y_true in [("Training Set", X_train, y_train), ("Validation Set", X_val, y_val), ("Test Set", X_test, y_test)]:
    y_pred = model.predict(dataset)
    mse = mean_squared_error(y_true, y_pred)
    mae = mean_absolute_error(y_true, y_pred)
    r2 = r2_score(y_true, y_pred)
    explained_variance = explained_variance_score(y_true, y_pred)

    print(f"Results on {name}:")
    print("Mean Squared Error (MSE):", mse)
    print("Mean Absolute Error (MAE):", mae)
    print("R-squared:", r2)
    print("Explained Variance:", explained_variance)
    print("-" * 20)